import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import SetRecording from "./SetRecording";
import RecordingScreen from "./RecordingScreen";
import TranscriptScreen from "./TranscriptScreen";
const Stack = createStackNavigator();

export default function App() {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="SetRecording" component={SetRecording} />
      <Stack.Screen name="RecordingScreen" component={RecordingScreen} />
      <Stack.Screen name="TranscriptScreen" component={TranscriptScreen} />
    </Stack.Navigator>
  );
}
