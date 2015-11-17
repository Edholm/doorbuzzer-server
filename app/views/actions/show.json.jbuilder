json.extract! @action, :id, :name, :description, :activated, :default_time, :created_at, :updated_at
json.execute_url execute_action_url(@action, format: :json)
