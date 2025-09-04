import { useState } from 'react'
import axios from 'axios'
import './PasswordChecker.css'

export default function PasswordChecker() {
    const [password, setPassword] = useState('')
    const [score, setScore] = useState<number | null>(null)

    const handleCheck = async() => {
        const response = await axios.post('http://localhost:5000/', { password })
        setScore(response.data.score)
    }

    const getStrengthClass = (score: number) => {
        if (score < 50) return 'weak'
        if (score < 80) return 'average'
        if (score < 100) return 'strong'
        return 'secure'
    }

    return (
        <div>
            <input 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                onKeyUp={handleCheck}
            />
            {score !== null && (
                <div className='score-display'>
                    <p className="strength-text">
                        {getStrengthClass(score)}
                    </p>
                    <img src={`../src/images/${getStrengthClass(score)}.png`} />
                    <p>Score: {score}</p>
                </div>
            )}
        </div>
    )

}
