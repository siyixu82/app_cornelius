import React, { Component } from "react";
import { Text, StyleSheet } from "react-native";
import {
  Container,
  Content,
  Icon,
  Picker,
  Form,
  Input,
  Title,
} from "native-base";
import { TouchableOpacity } from "react-native-gesture-handler";
import { createStackNavigator } from "@react-navigation/stack";

const Stack = createStackNavigator();

export default class SetRecording extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //facility: "key0",
      //physician: "key0",
      facility: "",
      physician: "",
      reason: "",
    };
  }
  onChangeFacility(value) {
    this.setState({
      ...this.state,
      facility: value,
    });
  }
  onChangePhysician(value) {
    this.setState({
      ...this.state,
      physician: value,
    });
  }
  render() {
    return (
      <Container style={styles.container}>
        <Title style={styles.title}>Before you start your recording</Title>
        <Content scrollEnabled={false}>
          <Text>Facility:</Text>
          <Input
            style={styles.input}
            onChangeText={(text) =>
              this.setState({ ...this.state, facility: text })
            }
          />
          {/* <Form>
            <Picker
              mode="dropdown"
              iosHeader="Select Facility"
              iosIcon={<Icon name="arrow-down" />}
              style={styles.input}
              selectedValue={this.state.facility}
              onValueChange={this.onChangeFacility.bind(this)}
            >
              <Picker.Item label="Duke Cancer" value="key0" />
              <Picker.Item label="Duke Radiology" value="key1" />
              <Picker.Item label="Duke Neurology" value="key2" />
              <Picker.Item label="Mayo Clinic Cancer" value="key3" />
              <Picker.Item label="Johns Hopkins Cancer" value="key4" />
            </Picker>
          </Form> */}
          <Text>Physician:</Text>
          <Input
            style={styles.input}
            onChangeText={(text) =>
              this.setState({ ...this.state, physician: text })
            }
          />
          {/* <Form>
            <Picker
              mode="dropdown"
              iosHeader="Select Doctor"
              iosIcon={<Icon name="arrow-down" />}
              style={styles.input}
              selectedValue={this.state.physician}
              onValueChange={this.onChangePhysician.bind(this)}
            >
              <Picker.Item label="Dr. Brown" value="key0" />
              <Picker.Item label="Dr. White" value="key1" />
              <Picker.Item label="Dr. Blue" value="key2" />
              <Picker.Item label="Dr. Purple" value="key3" />
              <Picker.Item label="Dr. Red" value="key4" />
            </Picker>
          </Form> */}
          <Text>Reason for Visit:</Text>
          <Input
            style={styles.input}
            onChangeText={(text) =>
              this.setState({ ...this.state, reason: text })
            }
          />
          <TouchableOpacity
            style={styles.startBtn}
            onPress={() => this.props.navigation.navigate("RecordingScreen")}
          >
            <Text style={styles.startText}>Start Your Recording</Text>
          </TouchableOpacity>
        </Content>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  input: {
    width: 200,
    borderWidth: 1.5,
    borderColor: "black",
    borderRadius: 5,
    margin: 10,
  },
  startText: {
    color: "white",
  },
  startBtn: {
    backgroundColor: "#6D9EEB",
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    marginBottom: 10,
  },
  title: {
    marginTop: "10%",
    marginBottom: "10%",
  },
});
