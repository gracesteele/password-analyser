import './App.css'
import PasswordChecker from './PasswordChecker'

function App() {

  return (
    <div className="container">
      <h1>Password Strength Checker</h1>
      <p>
        Type in your password to get visual feedback about the strength of your password.
      </p>

      <div className="password">
        <div className="password-prompt">Enter your password</div>
        <PasswordChecker />
      </div>
    </div>
  )
}

export default App
