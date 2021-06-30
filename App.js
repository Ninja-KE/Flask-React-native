import React from 'react'
import {View, StyleSheet} from 'react-native'
import Movies from './components/Movies'

const App = () => {
  return (
    <View style={styles.container}>
      <Movies/>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    flex: 1
  }
})

export default App