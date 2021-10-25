import {
  StyleSheet,
  Text,
  Image,
  ActivityIndicator,
  ScrollView,
  FlatList,
} from "react-native";
import { Container, Icon, View } from "native-base";
import React, { Component } from "react";
import { TouchableOpacity } from "react-native-gesture-handler";
import * as Permissions from "expo-permissions";
import * as FileSystem from "expo-file-system";
import { Audio } from "expo-av";
import { AppLoading } from "expo";
import { Asset } from "expo-asset";
import { readDirectoryAsync } from "expo-file-system";
import { createStackNavigator } from "@react-navigation/stack";
import Axios from "axios";

const Stack = createStackNavigator();

const styles = StyleSheet.compose({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  text: {
    width: "50%",
    margin: 20,
    fontSize: 18,
  },
  buttons: {
    flexDirection: "row",
  },
  screenIcon: {
    fontSize: 135,
    margin: 20,
  },
  endRecBtn: {
    margin: 15,
    fontSize: 60,
    color: "#FF0000",
  },
  startRecBtn: {
    margin: 15,
    fontSize: 60,
  },
  endText: {
    color: "white",
  },
  endBtn: {
    backgroundColor: "#6D9EEB",
    width: 100,
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    marginBottom: 10,
    fontSize: 30,
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    textAlign: "center",
  },
  scrollView: {
    height: "20%",
    width: "80%",
    margin: 20,
    alignSelf: "center",
    padding: 20,
    borderWidth: 5,
    borderRadius: 5,
  },
  contentConntainer: {
    justifyContent: "center",
    alignItems: "center",
    paddingBottom: 50,
  },
  loadingAnimation: {
    flex: 1,
    justifyContent: "center",
  },
  loadingHorizontal: {
    flexDirection: "row",
    justifyContent: "space-around",
    padding: 10,
  },
});

const recordingOptions = {
  android: {
    extension: ".m4a",
    outputFormat: Audio.RECORDING_OPTION_ANDROID_OUTPUT_FORMAT_MPEG_4,
    audioEncoder: Audio.RECORDING_OPTION_ANDROID_AUDIO_ENCODER_AAC,
    sampleRate: 44100,
    numberOfChannels: 1,
    bitRate: 128000,
  },
  ios: {
    extension: ".wav",
    audioQuality: Audio.RECORDING_OPTION_IOS_AUDIO_QUALITY_HIGH,
    sampleRate: 44100,
    numberOfChannels: 1,
    bitRate: 128000,
    linearPCMBitDepth: 16,
    linearPCMIsBigEndian: false,
    linearPCMIsFloat: false,
  },
};

class Record extends Component {
  constructor(props) {
    super(props);
    this.recording = null;
    this.state = {
      isFetching: false,
      isRecording: false,
      scriptAvailable: false,
      transcript: "",
    };
  }

  startRecording = async () => {
    // request permissions to record audio
    const { status } = await Permissions.askAsync(Permissions.AUDIO_RECORDING);
    // if the user doesn't allow us to do so - return as we can't do anything further :(
    if (status !== "granted") return;
    // when status is granted - setting up our state
    this.setState({ isRecording: true });
    // basic settings before we start recording,
    // you can read more about each of them in expo documentation on Audio
    await Audio.setAudioModeAsync({
      allowsRecordingIOS: true,
      interruptionModeIOS: Audio.INTERRUPTION_MODE_IOS_DO_NOT_MIX,
      playsInSilentModeIOS: true,
      interruptionModeAndroid: Audio.INTERRUPTION_MODE_ANDROID_DO_NOT_MIX,
      playThroughEarpieceAndroid: true,
    });
    const recording = new Audio.Recording();
    try {
      // here we pass our recording options
      await recording.prepareToRecordAsync(recordingOptions);
      // and finally start the record
      await recording.startAsync();
    } catch (error) {
      console.log(error);
      this.stopRecording();
    }

    // if recording was successful we store the result in variable,
    // so we can refer to it from other functions of our component

    //this.setState({ recording: recording })
    console.log(recording);
    this.recording = recording;
  };

  stopRecording = async () => {
    // set our state to false, so the UI knows that we've stopped the recording
    this.setState({ isRecording: false });
    try {
      // stop the recording
      await this.recording.stopAndUnloadAsync();
    } catch (error) {
      console.log(error);
    }
  };

  getTranscription = async () => {
    // set isFetching to true, so the UI knows about it
    this.setState({ isFetching: true });
    try {
      // take the uri of the recorded audio from the file system
      const { uri } = await FileSystem.getInfoAsync(this.recording.getURI());
      // console.log(uri);
      // now we create formData which will be sent to our backend
      const formData = new FormData();
      formData.append("file", {
        uri,
        // as different audio types are used for android and ios - we should handle it
        type: Platform.OS === "ios" ? "audio/x-wav" : "audio/m4a",
        name: Platform.OS === "ios" ? `${Date.now()}.wav` : `${Date.now()}.m4a`,
      });
      console.log(formData);
      // post the formData to our backend
      // add actual URL endpoint
      //here we are hardcodingn to mid7 because have not set up get request for meeting info endpoint to recieve dynnamic mid
      const { data } = await Axios.post(
        "https://cool-wharf-291516.ue.r.appspot.com/meeting/mid7/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // console.log(data.detail);
      // set transcript from the data which we received from the api
      this.setState({ transcript: data.detail });

      // Axios.post("https://cool-wharf-291516.ue.r.appspot.com/meeting/pid", {

      // }).then(res => {
      //   Axios.post("https://cool-wharf-291516.ue.r.appspot.com/meeting/mid".concat(res.mid), formData, {
      //     headers: {
      //       'Content-Type': 'multipart/form-data',
      //     },
      //   }).then(({ data }) => {
      //     this.setState({ transcript: data.transcript })
      //   })
      // })
    } catch (error) {
      console.log("There was an error reading file", error);
      this.stopRecording();
      // we will take a closer look at resetRecording function further down
      this.resetRecording();
    }
    // set isFetching to false so the UI can properly react on that
    this.setState({ isFetching: false });
    this.setState({ scriptAvailable: true });
  };

  deleteRecordingFile = async () => {
    // deleting file
    try {
      const info = await FileSystem.getInfoAsync(this.recording.getURI());
      await FileSystem.deleteAsync(info.uri);
    } catch (error) {
      console.log("There was an error deleting recorded file", error);
    }
  };

  resetRecording = () => {
    this.deleteRecordingFile();
    this.recording = null;
  };

  handleOnPressOut = () => {
    // first we stop the recording
    this.stopRecording();
    // second we interact with our backend
    this.getTranscription();
  };

  render() {
    const { isRecording, transcript, isFetching } = this.state;

    let icon = this.state.isRecording ? (
      <TouchableOpacity onPress={() => this.stopRecording()}>
        <Icon type="FontAwesome" name="microphone" style={styles.endRecBtn} />
      </TouchableOpacity>
    ) : (
      <TouchableOpacity onPress={() => this.startRecording()}>
        <Icon type="FontAwesome" name="microphone" style={styles.startRecBtn} />
      </TouchableOpacity>
    );

    if (this.state.isFetching) {
      return (
        <ActivityIndicator
          size="large"
          color="#6D9EEB"
          style={[styles.loadingAnimation, styles.loadingHorizontal]}
        />
      );
    }

    return (
      <Container style={styles.container}>
        <ScrollView
          style={styles.ScrollView}
          contentContainerStyle={styles.contentConntainer}
        >
          <Icon type="FontAwesome" name="comments" style={styles.screenIcon} />
          <Text style={styles.paragraph}>
            Let your doctor know you are recording, then hit the microphone
            button to start. Hit the microphone button to stop your recording,
            and the end button when you are finished.
          </Text>
          <View style={styles.buttons}>{icon}</View>
          <Text style={styles.text}>
            {isRecording ? "Recording..." : "Press button to start"}
          </Text>
          <TouchableOpacity
            style={styles.endBtn}
            // onPress={async () => {
            //   const { uri } = await FileSystem.getInfoAsync(
            //     this.recording.getURI()
            //   );
            //   console.log(uri);
            // }}
            onPress={() => this.handleOnPressOut()}
          >
            <Text style={styles.endText}> Done</Text>
          </TouchableOpacity>
          {this.state.scriptAvailable && (
            <TouchableOpacity
              style={styles.endBtn}
              onPress={() =>
                this.props.navigation.navigate("TranscriptScreen", {
                  //script: data.detail,
                  script: transcript,
                })
              }
            >
              <Text style={styles.endText}>View Journal</Text>
            </TouchableOpacity>
          )}
        </ScrollView>
      </Container>
    );
  }

  //<Text>{`${transcript}`}</Text>
  // async _cacheResourcesAsync() {
  //   const images = [require("splash.png")];

  //   const cacheImages = images.map(image => {
  //     return Asset.fromModule(image).downloadAsync();
  //   });
  //   return Promise.all(cacheImages);
  // }
}

export default Record;
