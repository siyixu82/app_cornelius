import "react-native-gesture-handler";
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import LoginScreen from "./screens/Login/LoginScreen";
import SignUpScreen from "./screens/SignUp/SignUpScreen";
import MainScreenNavigator from "./screens/Content/index";
import reducer from "./store/reducer";
import { createStore } from 'redux';
import { Provider } from 'react-redux'

const Stack = createStackNavigator();
const store = createStore(reducer);

export default function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="SignUp" component={SignUpScreen} />
          <Stack.Screen name="Landing" component={MainScreenNavigator} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  );
}
