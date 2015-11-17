json.array!(@action) do |action|
  json.extract! action, :id, :name, :description, :activated, :default_time
  json.execute_url execute_action_url(action, format: :json)
end
