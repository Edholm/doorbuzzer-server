class ActionsController < ApplicationController
  before_action :set_action, only: [:show, :edit, :update, :destroy, :unlock]
  #before_action :doorkeeper_authorize!, only: :unlock

  respond_to :html, :json

  def index
    @actions = Action.all
    respond_with(@action)
  end

  def show
    respond_with(@action)
  end

  def new
    @action = Action.new
    respond_with(@action)
  end

  def edit
  end

  def create
    @action = Action.new(action_params)
    @action.save
    respond_with(@action)
  end

  def update
    @action.update(action_params)
    respond_with(@action)
  end

  def destroy
    @action.destroy
    respond_with(@action)
  end

  def execute
    # Send the unlock command.
    # TODO: send the unlock command ;)
    @response = true, "OK"
    respond_with(@action)
  end

  private
    def set_action
      @action = Action.find(params[:id])
    end

    def action_params
      params.require(:a).permit(:name, :description, :activated, :implementation, :api_key, :default_time, :host, :port)
    end
end
