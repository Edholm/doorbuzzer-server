require 'test_helper'

class DoorbuzzersControllerTest < ActionController::TestCase
  setup do
    @doorbuzzer = doorbuzzers(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:doorbuzzers)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create doorbuzzer" do
    assert_difference('Doorbuzzer.count') do
      post :create, doorbuzzer: { activated: @doorbuzzer.activated, default_time: @doorbuzzer.default_time, description: @doorbuzzer.description, host: @doorbuzzer.host, name: @doorbuzzer.name, password: @doorbuzzer.password, port: @doorbuzzer.port }
    end

    assert_redirected_to doorbuzzer_path(assigns(:doorbuzzer))
  end

  test "should show doorbuzzer" do
    get :show, id: @doorbuzzer
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @doorbuzzer
    assert_response :success
  end

  test "should update doorbuzzer" do
    patch :update, id: @doorbuzzer, doorbuzzer: { activated: @doorbuzzer.activated, default_time: @doorbuzzer.default_time, description: @doorbuzzer.description, host: @doorbuzzer.host, name: @doorbuzzer.name, password: @doorbuzzer.password, port: @doorbuzzer.port }
    assert_redirected_to doorbuzzer_path(assigns(:doorbuzzer))
  end

  test "should destroy doorbuzzer" do
    assert_difference('Doorbuzzer.count', -1) do
      delete :destroy, id: @doorbuzzer
    end

    assert_redirected_to doorbuzzers_path
  end
end
