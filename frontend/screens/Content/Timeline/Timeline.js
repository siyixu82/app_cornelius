import React, { useState, useEffect } from "react";
import Axios from "axios";
import { View, Text, StyleSheet, ScrollView } from "react-native";
import { Card } from "react-native-elements";
import { TouchableOpacity } from "react-native-gesture-handler";
import {
  Container,
  Header,
  Content,
  Button,
  Icon,
  Item,
  Input,
} from "native-base";

const styles = StyleSheet.create({
  name: {
    textAlign: "center",
    flex: 1,
    fontSize: 14,
  },
  background: {
    backgroundColor: "#ececec",
  },
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
});

const Timeline = ({ navigation }) => {
  const [visitState, setVisits] = useState({
    visits: [],
  });
  useEffect(() => {
    Axios.get("https://cool-wharf-291516.ue.r.appspot.com/meeting/pid1/").then(
      (res) => {
        setVisits({
          visits: res.data,
        });
      }
    );
  }, []);

  return (
    <Container>
      <Header searchBar rounded>
        <Item>
          <Icon name="ios-search" />
          <Input placeholder="Search" />
        </Item>
        <Button transparent>
          <Text>Search</Text>
        </Button>
      </Header>
      <Content style={styles.background}>
        <ScrollView>
          <Card.Title style={styles.title}>Appointments</Card.Title>
          {visitState.visits.map((u, i) => {
            return (
              <Card key={i} style={styles.visit}>
                <TouchableOpacity
                  onPress={() => {
                    navigation.navigate("VisitJournal", {
                      data: u,
                    });
                  }}
                >
                  <Card.Title>{u.date}</Card.Title>
                  <View>
                    <Text style={styles.name}>{u.Doctor}</Text>
                    <Text style={styles.name}>{u.Facility}</Text>
                  </View>
                </TouchableOpacity>
              </Card>
            );
          })}
        </ScrollView>
      </Content>
    </Container>
  );
};

export default Timeline;
