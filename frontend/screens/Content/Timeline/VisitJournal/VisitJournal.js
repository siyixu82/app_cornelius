import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Card } from "react-native-elements";

const styles = StyleSheet.create({
title: {
    marginTop: 25,
    fontSize: 25
  },
  visit: {
    flexDirection: "row",
    marginTop: 20,
    marginBottom: 20,
    alignItems: "center",
  },
  text: {
      fontSize: 20,
  }
});

const VisitJournal = ({ route, navigation }) => {
    const { data } = route.params;
    return (
        <View style={{justifyContent: 'center' }}>
            <Card.Title style={styles.title}>Visit on {data.date}</Card.Title>
            <Card style={styles.visit}>
                <Text style={styles.text}>Appointment with {data.Doctor} </Text>
                <Text style={styles.text}>Seen at {data.Facility}</Text>
            </Card>
            <Card style={styles.visit}>
                <Text style={styles.text}>Transcription: Loading...</Text>
            </Card>
        </View>
    )
}

export default VisitJournal;