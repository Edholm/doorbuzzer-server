class RenamePasswordToApiKey < ActiveRecord::Migration
  def change
    rename_column :doorbuzzers, :password, :api_key
  end
end
