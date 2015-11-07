class DoorbuzzersController < ApplicationController
  before_action :set_doorbuzzer, only: [:show, :edit, :update, :destroy]
  before_action :doorkeeper_authorize!, only: :unlock 

  respond_to :html, :json

  def index
    @doorbuzzers = Doorbuzzer.all
    respond_with(@doorbuzzer)
  end

  def show
    respond_with(@doorbuzzer)
  end

  def new
    @doorbuzzer = Doorbuzzer.new
    respond_with(@doorbuzzer)
  end

  def edit
  end

  def create
    @doorbuzzer = Doorbuzzer.new(doorbuzzer_params)
    @doorbuzzer.save
    respond_with(@doorbuzzer)
  end

  def update
    @doorbuzzer.update(doorbuzzer_params)
    respond_with(@doorbuzzer)
  end

  def destroy
    @doorbuzzer.destroy
    respond_with(@doorbuzzer)
  end

  def unlock
    # Send the unlock command.
    # TODO: send the unlock command ;)
  end

  private
    def set_doorbuzzer
      @doorbuzzer = Doorbuzzer.find(params[:id])
    end

    def doorbuzzer_params
      params.require(:doorbuzzer).permit(:name, :description, :activated, :api_key, :default_time, :host, :port)
    end
end
