class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :name
      t.string :username
      t.string :uni
      t.string :faculty
      t.string :department
      t.string :grade
      t.string :year

      t.timestamps
    end
  end
end
