import { StyleSheet, Text, View, ScrollView, Image } from 'react-native'; 
import { Button } from 'react-native-elements'; 
 
export default function About({route, navigation}) { 
  return ( 
    <ScrollView>
    <View style={styles.container}> 
      <Image 
        style={styles.logo} 
        source={require('./assets/logo2.png')} 
      /> 
      <Text style={styles.title}>About</Text> 
      <Text style={styles.subtitle}>This app will alert you in case of 
      public sightings of potentially deadly weapons in your area. 
      You will be able to set a radius for which you want to receive alerts. 
      The backend of the app works by using a custom trained machine learning 
      model to detect guns or knives. This app was developed by team Blended 
      and Blended reserves all rights to the source code.
.</Text> 
      <Button 
        title="Get Started" 
        containerStyle={styles.buttonContainer} 
        buttonStyle={styles.button} 
        onPress={() => navigation.navigate('Radius')} 
      /> 
    </View> 
    </ScrollView>
  ); 
}; 
 
const styles = StyleSheet.create({ 
  container: { 
    flex: 1, 
    backgroundColor: '#fff', 
    alignItems: 'center', 
    justifyContent: 'center', 
  }, 
  logo: { 
    width: 200, 
    height: 200, 
  }, 
  title: { 
    fontSize: 30, 
    fontWeight: 'bold', 
    marginTop: 20, 
  }, 
  subtitle: { 
    fontSize: 20, 
    marginHorizontal: 40, 
    textAlign: 'center', 
    marginTop: 10, 
  }, 
  buttonContainer: { 
    marginTop: 20, 
    paddingBottom: 30
  }, 
  button: { 
    backgroundColor: '#2196F3', 
    borderRadius: 10, 
    paddingHorizontal: 20, 
    paddingVertical: 10
  }, 
});