import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import UserProfile from "./UserProfile";
import DoctorProfile from "./DoctorProfile";
const Stack = createStackNavigator();

export default function App() {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="UserProfile" component={UserProfile} />
      <Stack.Screen name="DoctorProfile" component={DoctorProfile} />
    </Stack.Navigator>
  );
}