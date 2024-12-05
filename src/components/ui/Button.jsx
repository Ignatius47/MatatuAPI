import { motion } from 'framer-motion';

function Button({ children, variant = 'primary', className = '', ...props }) {
  const baseClasses = 'px-4 py-2 rounded-lg font-medium transition-all duration-300 hover-lift';
  
  const variants = {
    primary: 'bg-primary-500 text-background hover:bg-primary-400 neon-glow',
    secondary: 'bg-secondary-500 text-white hover:bg-secondary-400 neon-glow',
    outline: 'border border-primary-500 text-primary-500 hover:bg-primary-500/10',
    ghost: 'text-text hover:bg-white/5',
  };

  return (
    <motion.button
      whileTap={{ scale: 0.95 }}
      className={`${baseClasses} ${variants[variant]} ${className}`}
      {...props}
    >
      {children}
    </motion.button>
  );
}

export default Button;