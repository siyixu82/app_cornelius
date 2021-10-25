import { View, Text, StyleSheet } from 'react-native';
import React from 'react';
import { Card } from 'react-native-elements';
const styles = StyleSheet.create({
    name: {
        flex: 1,
        justifyContent: "center",
    },
    title: {
        textAlign: "center",
        fontSize: 32,
        fontWeight: "600",
        marginBottom: 40
    },
    info: {
        flex: 1,
        justifyContent: "center",
    },
    field: {
        fontSize: 20,
        marginBottom: 10
    },
    value: {
        fontSize: 24
    },
    divider: {
        margin: 15
    }
})

const DoctorProfile = ({ route }) => {
    const { data } = route.params;
    return (
        <>
            <View style={styles.name}>
                <Text style={styles.title}>
                    {data.name}
                </Text>
                <Card style={{alignItems: "left"}}>
                    <Text style={styles.field}>Institution</Text>
                    <Text style={styles.value}>{data.institution}</Text>
                    <Card.Divider style={styles.divider}/>
                    <Text style={styles.field}>Contact Information</Text>
                    <Text style={styles.value}>Phone: {data.phone}</Text>
                    <Text style={styles.value}>Email: {data.email}</Text>
                    <Card.Divider style={styles.divider}/>
                    <Text style={styles.field}>Most recent visit</Text>
                    <Text style={styles.value}>{data.recent_visit}</Text>
                </Card>
            </View>
        </>
    )
}

export default DoctorProfile