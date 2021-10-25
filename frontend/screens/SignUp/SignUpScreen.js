import React, { Component } from "react";
import { connect } from "react-redux";
import {
  Alert,
  TextInput,
  View,
  StyleSheet,
  Text,
  TouchableOpacity,
  Image,
} from "react-native";
import * as ActionTypes from "../../store/actions";
import Axios from 'axios';


const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#ecf0f1",
  },
  input: {
    width: 200,
    height: 44,
    padding: 10,
    borderWidth: 1,
    borderColor: "black",
    marginBottom: 10,
  },
  login: {
    fontSize: 11,
  },
  inputView: {
    width: "80%",
    borderColor: "#000000",
    borderRadius: 5,
    borderWidth: 1,
    height: 50,
    marginBottom: 20,
    justifyContent: "center",
    padding: 20,
  },
  logo: {
    fontWeight: "bold",
    fontSize: 50,
    color: "#fb5b5a",
    marginBottom: 40,
  },
  inputText: {
    height: 50,
  },
  signUpButton: {
    width: "80%",
    backgroundColor: "#6D9EEB",
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    marginBottom: 10,
  },
  signUpText: {
    color: "white",
  },
});


class SignUpScreen extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      password2: "",
      firstname: "",
      lastname: ""
    };
  }

  onLogin() {
    this.props.navigation.navigate("Login");
  }

  onSignUp() {
    const {
      email,
      password,
      password2,
      firstname,
      lastname,
    } = this.state;
    Axios.post("https://cool-wharf-291516.ue.r.appspot.com/signup/", {
      first_name: firstname,
      last_name: lastname,
      email: email,
      password: password,
      role: "P"
    }).then(res => {
      this.props.onSetId(res.data.uid)
      this.props.navigation.navigate("Landing");
    })
  }

  render() {
    return (
      <View style={styles.container}>
        <View>
          <Image source={require('../../assets/logo.png')} style={{height: 250, width: 250}} />
        </View>
        <View style={styles.inputView}>
          <TextInput
            value={this.state.firstname}
            style={styles.inputText}
            onChangeText={(text) => this.setState({ firstname: text })}
            placeholder={"First Name"}
          />
        </View>
        <View style={styles.inputView}>
          <TextInput
            value={this.state.lastname}
            style={styles.inputText}
            onChangeText={(text) => this.setState({ lastname: text })}
            placeholder={"Last Name"}
          />
        </View>
        <View style={styles.inputView}>
          <TextInput
            value={this.state.email}
            style={styles.inputText}
            onChangeText={(text) => this.setState({ email: text })}
            placeholder={"Email"}
          />
        </View>
        <View style={styles.inputView}>
          <TextInput
            value={this.state.password}
            style={styles.inputText}
            onChangeText={(text) => this.setState({ password: text })}
            placeholder={"Password"}
            secureTextEntry={true}
          />
        </View>
        <View style={styles.inputView}>
          <TextInput
            value={this.state.password2}
            style={styles.inputText}
            onChangeText={(text) => this.setState({ password2: text })}
            placeholder={" Re-enter Password"}
            secureTextEntry={true}
          />
        </View>
        <TouchableOpacity onPress={this.onLogin.bind(this)}>
          <Text style={styles.login}>Already have an account? Log in</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.signUpButton}
          onPress={this.onSignUp.bind(this)}
        >
          <Text style={styles.signUpText}>SignUp</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    onSetId: (uid) => dispatch({ type: ActionTypes.SET_ID, val: uid }),
  }
}

export default connect(null, mapDispatchToProps)(SignUpScreen)