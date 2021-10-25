import { Container, Icon } from "native-base";
import { Card, ListItem } from "react-native-elements";
import { StyleSheet, Text, View } from "react-native";
import React, { useState } from "react";
import { TouchableOpacity } from "react-native-gesture-handler";
import { connect } from "react-redux";

const styles = StyleSheet.create({
  card: {
    display: "flex",
    flexDirection: "row",
    alignItems: "center",
  },
  edit: {
    color: "#6D9EEB",
  },
  icon: {
    fontSize: 50,
    margin: 20,
  },
});

// in the future get all the profile data from an API call
const Profile = (props, { navigation }) => {

  const [showState, setShowState] = useState(false);

  const lst = [
    {
      name: 'Dr. White',
      institution: 'Duke Neurology',
      phone: '919-222-2222',
      email: 'dwhite@duke.edu',
      recent_visit: '10-20-2020'
    },
    {
      name: 'Dr. Red',
      institution: 'Duke Cancer',
      phone: '919-222-2222',
      email: 'dred@duke.edu',
      recent_visit: '10-09-2020'
    }, 
    {
      name: 'Dr. Blue',
      institution: 'Duke Radiology',
      phone: '919-222-2222',
      email: 'dblue@duke.edu',
      recent_visit: '09-23-2020'
    }
  ]

  const doctors = showState?  
    lst.map((u, i) => {
      return (
        <ListItem key={i} bottomDivider onPress={() => navigation.navigate("DoctorProfile", {data: u})}>
          <ListItem.Content>
            <ListItem.Title>{u.name}</ListItem.Title>
            <ListItem.Subtitle>{u.institution}</ListItem.Subtitle>
          </ListItem.Content>
        </ListItem>
      );
    }) :
    <View />

  return (
    <Container>
      <Card>
        <View style={styles.card}>
          <Icon type="FontAwesome" name="user" style={styles.icon} />
          <View>
            <Card.Title>{props.firstname + " " + props.lastname}</Card.Title>
            <TouchableOpacity>
              <Text style={styles.edit}>Edit</Text>
            </TouchableOpacity>
          </View>
        </View>
        <Text>Email: {props.email}</Text>
      </Card>
      <Card>
        <TouchableOpacity onPress={() => setShowState(!showState)}>
        <View style={styles.card}>
          <Icon type="FontAwesome" name="user-md" style={styles.icon} />
          <View>
            <Card.Title>My Doctors</Card.Title>
            <Text>{lst.length} Doctors</Text>
          </View>
        </View>
        </TouchableOpacity>
        {doctors}
      </Card>
      <Card>
        <TouchableOpacity>
          <View style={styles.card}>
            <Icon type="FontAwesome" name="id-card" style={styles.icon} />
            <View>
              <Card.Title>My Insurance Plan</Card.Title>
              <Text>1 Linked Plan</Text>
            </View>
          </View>
        </TouchableOpacity>
      </Card>
    </Container>
  );
};

const mapStateToProps = (state) => {
  return {
    uid: state.uid,
    firstname: state.firstname,
    lastname: state.lastname,
    email: state.email
  };
};

export default connect(mapStateToProps)(Profile);
