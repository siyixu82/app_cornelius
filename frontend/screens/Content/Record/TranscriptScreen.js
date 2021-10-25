import React, { Component } from "react";
import { View, Text, StyleSheet } from "react-native";
import { Card } from "react-native-elements";
import { createStackNavigator } from "@react-navigation/stack";
import axios from "axios";

const Stack = createStackNavigator();

const styles = StyleSheet.create({
  title: {
    marginTop: 25,
    fontSize: 25,
  },
  visit: {
    flexDirection: "row",
    marginTop: 20,
    marginBottom: 20,
    alignItems: "center",
  },
  text: {
    fontSize: 20,
  },
});

class TranscriptScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      script: "Loading...",
    };
  }
  componentDidMount() {
    this.getTranscript();
  }

  getTranscript() {
    //const TranscriptScreen = ({ route, navigation }) => {
    //const { transcript } = route.params;
    axios
      .get("https://cool-wharf-291516.ue.r.appspot.com/meeting/mid7/")
      .then((res) => {
        if (res.status == "200") {
          this.setState({ script: res.data.script });
        }
      });
  }

  render() {
    return (
      <View style={{ justifyContent: "center" }}>
        <Card.Title style={styles.title}>Visit on today </Card.Title>
        <Card style={styles.visit}>
          <Text style={styles.text}>Appointment with your doctor </Text>
          <Text style={styles.text}>Seen at the facility</Text>
        </Card>
        <Card style={styles.visit}>
          <Text style={styles.text}> {JSON.stringify(this.state.script)}</Text>
        </Card>
      </View>
    );
  }
}

export default TranscriptScreen;
