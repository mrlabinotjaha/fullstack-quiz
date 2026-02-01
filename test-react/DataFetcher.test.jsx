import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import DataFetcher from './DataFetcher';

const originalError = console.error;

beforeAll(() => {
  console.error = (...args) => {
    if (typeof args[0] === 'string' && args[0].includes('not wrapped in act')) return;
    originalError.call(console, ...args);
  };
});

afterAll(() => {
  console.error = originalError;
});

beforeEach(() => {
  global.fetch = jest.fn();
});

afterEach(() => {
  jest.restoreAllMocks();
});

test('shows loading state initially', () => {
  fetch.mockReturnValue(new Promise(() => {}));
  render(<DataFetcher />);
  expect(screen.getByText('Loading...')).toBeInTheDocument();
});

test('renders data after successful fetch', async () => {
  fetch.mockResolvedValue({
    json: () =>
      Promise.resolve({
        title: 'Buy groceries',
        completed: false,
      }),
  });

  render(<DataFetcher />);

  await waitFor(() => {
    expect(screen.getByText('Buy groceries')).toBeInTheDocument();
  });
  expect(screen.getByText('Completed: No')).toBeInTheDocument();
});

test('renders completed Yes when todo is completed', async () => {
  fetch.mockResolvedValue({
    json: () =>
      Promise.resolve({
        title: 'Walk the dog',
        completed: true,
      }),
  });

  render(<DataFetcher />);

  await waitFor(() => {
    expect(screen.getByText('Walk the dog')).toBeInTheDocument();
  });
  expect(screen.getByText('Completed: Yes')).toBeInTheDocument();
});

test('renders error message on fetch failure', async () => {
  fetch.mockRejectedValue(new Error('Network error'));

  render(<DataFetcher />);

  await waitFor(() => {
    expect(screen.getByText('Error: Network error')).toBeInTheDocument();
  });
});

test('fetches from the correct URL', () => {
  fetch.mockResolvedValue({
    json: () => Promise.resolve({ title: 'Test', completed: false }),
  });

  render(<DataFetcher />);

  expect(fetch).toHaveBeenCalledWith(
    'https://jsonplaceholder.typicode.com/todos/1'
  );
});
