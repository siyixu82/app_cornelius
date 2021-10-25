import React, { Component } from "react";
import { connect } from "react-redux";
import * as ActionTypes from "../../store/actions";
import {
  Alert,
  TextInput,
  View,
  StyleSheet,
  TouchableOpacity,
  Text,
  Image,
} from "react-native";
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
  forgot: {
    fontSize: 11,
  },
  loginBtn: {
    width: "80%",
    backgroundColor: "#6D9EEB",
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    marginBottom: 10,
  },
  signUpBtn: {
    width: "80%",
    backgroundColor: "#C5C7C4",
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
  },
  btnText: {
    color: "white",
  },
  signUpText: {
    color: "black",
  },
});


class LoginScreen extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
    };
  }

  onLogin() {
    const { email, password } = this.state;
    Axios.post("https://cool-wharf-291516.ue.r.appspot.com/login/", {
      email,
      password,
    }).then(res => {
      this.props.onSetId(res.data.uid)
      this.props.navigation.navigate("Landing");
    })
    //this.props.navigation.navigate("Landing");
  }

  onSignUp() {
    const { email, password } = this.state;
    this.props.navigation.navigate("SignUp");
  }

  onForgot() {
    const { email, password } = this.state;
    Alert.alert("Forgot password pressed");
  }

  render() {
    return (
      <View style={styles.container}>
        <View>
          <Image source={require("../../assets/logo.png")} style={{height: 250, width: 250}} />
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
            onChangeText={(text) => this.setState({ password: text })}
            placeholder={"Password"}
            secureTextEntry={true}
            style={styles.inputText}
          />
        </View>
        <TouchableOpacity onPress={this.onForgot.bind(this)}>
          <Text style={styles.forgot}>Forgot Password?</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.loginBtn}
          onPress={this.onLogin.bind(this)}
        >
          <Text style={styles.btnText}>Login</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.signUpBtn} onPress={this.onSignUp.bind(this)}>
          <Text style={styles.btnText}>Sign Up</Text>
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

export default connect(null, mapDispatchToProps)(LoginScreen)