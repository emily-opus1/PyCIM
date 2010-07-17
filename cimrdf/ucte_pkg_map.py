# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" Defines a map of class names to their module.
"""

ucte_pkg_map = {
    "IEC61970CIMVersion": "ucte",
    "Element": "ucte",
    "IdentifiedObject": "ucte.core",
    "PowerSystemResource": "ucte.core",
    "Equipment": "ucte.core",
    "ConductingEquipment": "ucte.core",
    "Curve": "ucte.core",
    "BasicIntervalSchedule": "ucte.core",
    "IrregularIntervalSchedule": "ucte.core",
    "RegularIntervalSchedule": "ucte.core",
    "ConnectivityNodeContainer": "ucte.core",
    "EquipmentContainer": "ucte.core",
    "CurveData": "ucte.core",
    "Bay": "ucte.core",
    "PSRType": "ucte.core",
    "GeographicalRegion": "ucte.core",
    "Terminal": "ucte.core",
    "OperatingParticipant": "ucte.core",
    "VoltageLevel": "ucte.core",
    "BasePower": "ucte.core",
    "Unit": "ucte.core",
    "ModelingAuthority": "ucte.core",
    "BaseVoltage": "ucte.core",
    "SubGeographicalRegion": "ucte.core",
    "PsrList": "ucte.core",
    "Substation": "ucte.core",
    "ReportingGroup": "ucte.core",
    "Company": "ucte.core",
    "ReportingSuperGroup": "ucte.core",
    "RegularTimePoint": "ucte.core",
    "IrregularTimePoint": "ucte.core",
    "ModelingAuthoritySet": "ucte.core",
    "OperatingShare": "ucte.core",
    "PowerTransformer": "ucte.wires",
    "RegulatingCondEq": "ucte.wires",
    "FrequencyConverter": "ucte.wires",
    "ShuntCompensator": "ucte.wires",
    "HeatExchanger": "ucte.wires",
    "RegulatingControl": "ucte.wires",
    "ReactiveCapabilityCurve": "ucte.wires",
    "Line": "ucte.wires",
    "Connector": "ucte.wires",
    "Junction": "ucte.wires",
    "Ground": "ucte.wires",
    "Conductor": "ucte.wires",
    "TransformerWinding": "ucte.wires",
    "WireArrangement": "ucte.wires",
    "EnergyConsumer": "ucte.wires",
    "Switch": "ucte.wires",
    "ProtectedSwitch": "ucte.wires",
    "LoadBreakSwitch": "ucte.wires",
    "ACLineSegment": "ucte.wires",
    "Plant": "ucte.wires",
    "WireType": "ucte.wires",
    "RegulationSchedule": "ucte.wires",
    "WindingTest": "ucte.wires",
    "MutualCoupling": "ucte.wires",
    "Disconnector": "ucte.wires",
    "SeriesCompensator": "ucte.wires",
    "GroundDisconnector": "ucte.wires",
    "SynchronousMachine": "ucte.wires",
    "CompositeSwitch": "ucte.wires",
    "TapChanger": "ucte.wires",
    "PhaseTapChanger": "ucte.wires",
    "RectifierInverter": "ucte.wires",
    "StaticVarCompensator": "ucte.wires",
    "RatioTapChanger": "ucte.wires",
    "ConductorType": "ucte.wires",
    "VoltageControlZone": "ucte.wires",
    "EnergySource": "ucte.wires",
    "Fuse": "ucte.wires",
    "Jumper": "ucte.wires",
    "DCLineSegment": "ucte.wires",
    "Breaker": "ucte.wires",
    "BusbarSection": "ucte.wires",
    "TopologicalIsland": "ucte.topology",
    "ConnectivityNode": "ucte.topology",
    "TopologicalNode": "ucte.topology",
    "BusNameMarker": "ucte.topology",
    "ClearanceTag": "ucte.outage",
    "ClearanceTagType": "ucte.outage",
    "OutageSchedule": "ucte.outage",
    "SwitchingOperation": "ucte.outage",
    "SteamSupply": "ucte.generation.generation_dynamics",
    "FossilSteamSupply": "ucte.generation.generation_dynamics",
    "HeatRecoveryBoiler": "ucte.generation.generation_dynamics",
    "PWRSteamSupply": "ucte.generation.generation_dynamics",
    "PrimeMover": "ucte.generation.generation_dynamics",
    "Supercritical": "ucte.generation.generation_dynamics",
    "CombustionTurbine": "ucte.generation.generation_dynamics",
    "HydroTurbine": "ucte.generation.generation_dynamics",
    "Subcritical": "ucte.generation.generation_dynamics",
    "CTTempActivePowerCurve": "ucte.generation.generation_dynamics",
    "SteamTurbine": "ucte.generation.generation_dynamics",
    "DrumBoiler": "ucte.generation.generation_dynamics",
    "BWRSteamSupply": "ucte.generation.generation_dynamics",
    "LevelVsVolumeCurve": "ucte.generation.production",
    "FossilFuel": "ucte.generation.production",
    "SteamSendoutSchedule": "ucte.generation.production",
    "EmissionCurve": "ucte.generation.production",
    "CombinedCyclePlant": "ucte.generation.production",
    "StartIgnFuelCurve": "ucte.generation.production",
    "HydroGeneratingEfficiencyCurve": "ucte.generation.production",
    "StartRampCurve": "ucte.generation.production",
    "GeneratingUnit": "ucte.generation.production",
    "NuclearGeneratingUnit": "ucte.generation.production",
    "WindGeneratingUnit": "ucte.generation.production",
    "StartMainFuelCurve": "ucte.generation.production",
    "StartupModel": "ucte.generation.production",
    "AirCompressor": "ucte.generation.production",
    "HeatInputCurve": "ucte.generation.production",
    "CogenerationPlant": "ucte.generation.production",
    "ShutdownCurve": "ucte.generation.production",
    "InflowForecast": "ucte.generation.production",
    "TargetLevelSchedule": "ucte.generation.production",
    "HydroGeneratingUnit": "ucte.generation.production",
    "EmissionAccount": "ucte.generation.production",
    "GrossToNetActivePowerCurve": "ucte.generation.production",
    "HydroPumpOpSchedule": "ucte.generation.production",
    "Reservoir": "ucte.generation.production",
    "CAESPlant": "ucte.generation.production",
    "GenUnitOpCostCurve": "ucte.generation.production",
    "PenstockLossCurve": "ucte.generation.production",
    "HydroPump": "ucte.generation.production",
    "GenUnitOpSchedule": "ucte.generation.production",
    "FuelAllocationSchedule": "ucte.generation.production",
    "HeatRateCurve": "ucte.generation.production",
    "IncrementalHeatRateCurve": "ucte.generation.production",
    "ThermalGeneratingUnit": "ucte.generation.production",
    "TailbayLossCurve": "ucte.generation.production",
    "HydroPowerPlant": "ucte.generation.production",
    "PowerCutZone": "ucte.load_model",
    "LoadResponseCharacteristic": "ucte.load_model",
    "EnergyArea": "ucte.load_model",
    "LoadArea": "ucte.load_model",
    "StationSupply": "ucte.load_model",
    "SubLoadArea": "ucte.load_model",
    "ConformLoad": "ucte.load_model",
    "Load": "ucte.load_model",
    "NonConformLoad": "ucte.load_model",
    "InductionMotorLoad": "ucte.load_model",
    "LoadGroup": "ucte.load_model",
    "NonConformLoadGroup": "ucte.load_model",
    "Season": "ucte.load_model",
    "SeasonDayTypeSchedule": "ucte.load_model",
    "ConformLoadSchedule": "ucte.load_model",
    "NonConformLoadSchedule": "ucte.load_model",
    "CustomerLoad": "ucte.load_model",
    "DayType": "ucte.load_model",
    "ConformLoadGroup": "ucte.load_model",
    "OperationalLimit": "ucte.operational_limits",
    "CurrentLimit": "ucte.operational_limits",
    "BranchGroup": "ucte.operational_limits",
    "BranchGroupTerminal": "ucte.operational_limits",
    "ApparentPowerLimit": "ucte.operational_limits",
    "OperationalLimitSet": "ucte.operational_limits",
    "VoltageLimit": "ucte.operational_limits",
    "ActivePowerLimit": "ucte.operational_limits",
    "OperationalLimitType": "ucte.operational_limits",
    "Control": "ucte.meas",
    "Measurement": "ucte.meas",
    "StringMeasurement": "ucte.meas",
    "Discrete": "ucte.meas",
    "ValueAliasSet": "ucte.meas",
    "MeasurementValue": "ucte.meas",
    "DiscreteValue": "ucte.meas",
    "Limit": "ucte.meas",
    "AnalogLimit": "ucte.meas",
    "LimitSet": "ucte.meas",
    "AccumulatorLimitSet": "ucte.meas",
    "SetPoint": "ucte.meas",
    "Command": "ucte.meas",
    "StringMeasurementValue": "ucte.meas",
    "ValueToAlias": "ucte.meas",
    "ControlType": "ucte.meas",
    "AnalogLimitSet": "ucte.meas",
    "Accumulator": "ucte.meas",
    "AccumulatorLimit": "ucte.meas",
    "MeasurementValueSource": "ucte.meas",
    "AnalogValue": "ucte.meas",
    "Analog": "ucte.meas",
    "MeasurementType": "ucte.meas",
    "Quality61850": "ucte.meas",
    "MeasurementValueQuality": "ucte.meas",
    "AccumulatorValue": "ucte.meas",
    "RemotePoint": "ucte.scada",
    "RemoteControl": "ucte.scada",
    "RemoteUnit": "ucte.scada",
    "CommunicationLink": "ucte.scada",
    "RemoteSource": "ucte.scada",
    "StateVariable": "ucte.state_variables",
    "SvVoltage": "ucte.state_variables",
    "SvShuntCompensatorSections": "ucte.state_variables",
    "SvPowerFlow": "ucte.state_variables",
    "SvStatus": "ucte.state_variables",
    "SvTapStep": "ucte.state_variables",
    "SvInjection": "ucte.state_variables",
    "EquivalentEquipment": "ucte.equivalents",
    "EquivalentShunt": "ucte.equivalents",
    "EquivalentBranch": "ucte.equivalents",
    "EquivalentNetwork": "ucte.equivalents",
    "ContingencyElement": "ucte.contingency",
    "ContingencyEquipment": "ucte.contingency",
    "Contingency": "ucte.contingency",
    "RecloseSequence": "ucte.protection",
    "ProtectionEquipment": "ucte.protection",
    "CurrentRelay": "ucte.protection",
    "SynchrocheckRelay": "ucte.protection",
    "AltTieMeas": "ucte.control_area",
    "AltGeneratingUnitMeas": "ucte.control_area",
    "ControlArea": "ucte.control_area",
    "TieFlow": "ucte.control_area",
    "ControlAreaGeneratingUnit": "ucte.control_area",
}
