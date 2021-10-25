#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for async
batch processing.
Example usage:
    python transcribe_async.py resources/audio.raw
    python transcribe_async.py gs://cloud-samples-tests/speech/vr.flac
"""

import argparse
import io
import sys


# [START speech_transcribe_async]
def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech

    client = speech.SpeechClient()

    # [START speech_python_migration_async_request]
    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to 60 seconds audio.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    # [START speech_python_migration_async_response
    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    # [END speech_python_migration_async_request]
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))
    # [END speech_python_migration_async_response]


# [END speech_transcribe_async]


# [START speech_transcribe_async_gcs]
def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    script = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        # script = "".format(result.alternatives[0].transcript)
        script = script + result.alternatives[0].transcript
        # print(u"Transcript: {}".format(result.alternatives[0].transcript))
        # print("Confidence: {}".format(result.alternatives[0].confidence))
    print(script)
    return script
# [END speech_transcribe_async_gcs]


def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    # storage_client = storage.Client.from_service_account_json('/Users/kioritanaka/Downloads/Cornelius-9a072edab24f.json')


def upload_to_bucket(blob_name, file, bucket_name):
    """ Upload data to a bucket"""
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    # storage_client = storage.Client.from_service_account_json('/Users/kioritanaka/Downloads/Cornelius-9a072edab24f.json')

    storage_client = storage.Client()
    # print(buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_file(file, rewind=True)
    # returns a public url
    return 'gs://' + bucket_name + '/' + blob_name


# def decode_audio(in_filename, **input_kwargs):
    # parser = argparse.ArgumentParser(description='Convert speech audio to text using Google Speech API')
    # parser.add_argument('in_filename', help='Input filename (`-` for stdin)')
    # args = parser.parse_args()
    # in_filename = args.filename
    # try:
    #     out, err = (ffmpeg
    #         .input(in_filename, **input_kwargs)
    #         # .output('-', format='flac', acodec='flac', ac=1, ar='16k')
    #         .output('-', format='s16le', acodec='pcm_s16le', ac=1, ar='16k')
    #         .overwrite_output()
    #         .run(capture_stdout=True, capture_stderr=True)
    #     )
    # except ffmpeg.Error as e:
    #     print(e.stderr, file=sys.stderr)
    #     sys.exit(1)
    # return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "path", help="File or GCS path for audio file to be recognized")
    args = parser.parse_args()
    if args.path.startswith("gs://"):
        transcribe_gcs(args.path)
    else:
        transcribe_file(args.path)
