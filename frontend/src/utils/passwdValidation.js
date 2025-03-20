export const validatePassword = (password, passwordAgain, toast = undefined) => {
    if (password !== passwordAgain) {
        if (toast) {
            toast.error('Passwords do not match')
        }
        return false
    }
    if (password.length < 8) {
        if (toast) {
            toast.error(`Password must be at least 8 characters long.`)
        }
        return false
    }
    if (!password.match(/[a-z]/)) {
        if (toast) {
            toast.error('Password must contain at least one lowercase letter')
        }
        return false
    }
    if (!password.match(/[A-Z]/)) {
        if (toast) {
            toast.error('Password must contain at least one uppercase letter')
        }
        return false
    }
    if (!password.match(/[0-9]/)) {
        if (toast) {
            toast.error('Password must contain at least one digit')
        }
        return false
    }
    return true
}
