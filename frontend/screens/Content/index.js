import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as ActionTypes from "../../store/actions";
import Timeline from "./Timeline/index.js";
import SetRecording from "./Record/index.js";
import Profile from "./Profile/index.js";
import Axios from "axios";
import { StyleSheet, Image } from "react-native";
import { Header, Title, Container, Icon } from "native-base";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

const Tab = createBottomTabNavigator();

function App(props) {
  useEffect(() => {
    Axios.get("https://cool-wharf-291516.ue.r.appspot.com/user/uid".concat(props.uid)).then(res => {
      props.onSetFirstName(res.data.first_name)
      props.onSetLastName(res.data.last_name)
      props.onSetEmail(res.data.email)
      //props.onSetAddress(res.data.address)
      //props.onSetInsurance(res.data.insurance)
      //props.onSetRole(res.data.role)
    })
  }, [])
  return (
    <Container>
      <Header>
        <Image source={require("../../assets/logo_2.png")} style={{height: 75, width: 75}} />
      </Header>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ color, size }) => {
            let iconName;
            if (route.name === "Timeline") {
              iconName = "book";
            } else if (route.name === "SetRecording") {
              iconName = "plus-circle";
            } else if (route.name === "Profile") {
              iconName = "user-circle-o";
            }
            return (
              <Icon
                type="FontAwesome"
                name={iconName}
                size={size}
                style={{ color: color }}
              />
            );
          },
        })}
        tabBarOptions={{
          showLabel: false,
          activeTintColor: "#6D9EEB",
          inactiveTintColor: "gray",
        }}
      >
        <Tab.Screen name="Timeline" component={Timeline} />
        <Tab.Screen name="SetRecording" component={SetRecording} />
        <Tab.Screen name="Profile" component={Profile} />
      </Tab.Navigator>
    </Container>
  );
}

const mapStateToProps = (state) => {
  return {
    uid: state.uid,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    onSetFirstName: (first) => dispatch({ type: ActionTypes.SET_FIRSTNAME, val: first }),
    onSetLastName: (last) => dispatch({ type: ActionTypes.SET_LASTNAME, val: last }),
    onSetEmail: (email) => dispatch({ type: ActionTypes.SET_EMAIL, val: email }),
    onSetPhysicians: (physicians) => dispatch({ type: ActionTypes.SET_PHYSICIANS, val: physicians }),
    onSetFacilities: (facilities) => dispatch({ type: ActionTypes.SET_FACILITIES, val: facilities }),
    onSetJournals: (journals) => dispatch({ type: ActionTypes.SET_JOURNALS, val: journals })
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App)
