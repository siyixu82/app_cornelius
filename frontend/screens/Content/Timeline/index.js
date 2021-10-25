import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import Timeline from "./Timeline";
import VisitJournal from "./VisitJournal/VisitJournal";
const Stack = createStackNavigator();

export default function App() {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="Timeline" component={Timeline} />
      <Stack.Screen name="VisitJournal" component={VisitJournal} />
    </Stack.Navigator>
  );
}