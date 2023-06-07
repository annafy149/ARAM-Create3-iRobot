import React from 'react';
import { StyleSheet, Text, View, Button, Image, Linking } from 'react-native';

const Help = () => {
  const handleCall = () => {
    // Replace the phone number with your local emergency number
    const phoneNumber = '911';
    Linking.openURL(`tel:${phoneNumber}`);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Need Help?</Text>
      <Text style={styles.subtitle}>If you are in an emergency, please call 911 immediately.</Text>
      <Button
        title="Call 911"
        containerStyle={styles.buttonContainer}
        buttonStyle={styles.button}
        onPress={handleCall}
      />
      <Image
        style={styles.logo}
        source={require('./assets/help.png')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  logo: {
    width: 200,
    height: 200,
  },
  subtitle: {
    fontSize: 20,
    marginHorizontal: 40,
    textAlign: 'center',
    marginBottom: 20,
  },
  buttonContainer: {
    marginTop: 20,
  },
  button: {
    backgroundColor: '#2196F3',
    borderRadius: 10,
    paddingHorizontal: 20,
    paddingVertical: 10,
  },
});

export default Help;
