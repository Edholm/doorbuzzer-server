class RenameActionToImplementation < ActiveRecord::Migration
  def change
    rename_column :actions, :action, :implementation
  end
end
