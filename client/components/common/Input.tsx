import getTestIDs from '../../utils/getTestIds';

export const inputTestIds: ReturnType<typeof getTestIDs> & {
  error?: string;
  label?: string;
  input?: string;
} = getTestIDs();

interface IInput {
  id: string;
  label: string;
  name: string;
  value: string;
  handleInput: (e: React.ChangeEvent<HTMLInputElement>) => void;
  classes?: string;
  error?: string;
  placeholder?: string;
  type?: 'email' | 'input' | 'password';
}

export const Input: React.FC<IInput> = ({
  id,
  name,
  label,
  type = 'input',
  value,
  placeholder = '',
  handleInput,
  error = '',
  classes = '',
}) => {
  return (
    <div>
      <label htmlFor={name} data-testid={inputTestIds.label}>
        {label}
      </label>
      <input
        data-testid={inputTestIds.input}
        id={id}
        type={type}
        name={name}
        value={value}
        placeholder={placeholder}
        onInput={handleInput}
        className={classes}
      />
      {error && <div data-testid={inputTestIds.error}>{error}</div>}
    </div>
  );
};
