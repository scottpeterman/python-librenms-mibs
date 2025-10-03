# SNMP MIB module (BKTEL-HFC862-BES-V01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bktel\BKTEL-HFC862-BES-V01-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:20 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(DisplayString,
 ModuleWidthValue,
 NESlotValue,
 PerceivedSeverityValue,
 TruthValue,
 modules) = mibBuilder.importSymbols(
    "BKTEL-HFC862-BASE-MIB",
    "DisplayString",
    "ModuleWidthValue",
    "NESlotValue",
    "PerceivedSeverityValue",
    "TruthValue",
    "modules")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 experimental,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PortType(Integer32):
    """Custom type PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeCopper", 1),
          ("typeFiber", 2))
    )





class PortLinkState(Integer32):
    """Custom type PortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 1),
          ("linkUp", 2))
    )





class PortStatus(Integer32):
    """Custom type PortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("statusUnknown", 1),
          ("statusInit", 2),
          ("statusValid", 3),
          ("statusBusy", 4),
          ("statusEmpty", 5),
          ("statusInvalid", 6),
          ("statusLossOfSignal", 7))
    )





class PortDuplexMode(Integer32):
    """Custom type PortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplexFull", 1),
          ("duplexHalf", 2))
    )





class PortSpeed(Integer32):
    """Custom type PortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("speedUnknown", 0),
          ("speed10Mbps", 10),
          ("speed100Mbps", 100),
          ("speed1000Mbps", 1000))
    )





class PortFlowControl(Integer32):
    """Custom type PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowControlDisabled", 1),
          ("flowControlEnabled", 2))
    )





class NESlotWriteValue(Integer32):
    """Custom type NESlotWriteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bes_ObjectIdentity = ObjectIdentity
bes = _Bes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114)
)
_BesCommon_ObjectIdentity = ObjectIdentity
besCommon = _BesCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1)
)


class _BesCommonNumberOfModules_Type(Integer32):
    """Custom type besCommonNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_BesCommonNumberOfModules_Type.__name__ = "Integer32"
_BesCommonNumberOfModules_Object = MibScalar
besCommonNumberOfModules = _BesCommonNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 1),
    _BesCommonNumberOfModules_Type()
)
besCommonNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besCommonNumberOfModules.setStatus("mandatory")
_BesCommonTable_Object = MibTable
besCommonTable = _BesCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2)
)
if mibBuilder.loadTexts:
    besCommonTable.setStatus("mandatory")
_BesCommonEntry_Object = MibTableRow
besCommonEntry = _BesCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1)
)
besCommonEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besCommonEntry.setStatus("mandatory")
_BesNESlot_Type = NESlotValue
_BesNESlot_Object = MibTableColumn
besNESlot = _BesNESlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 1),
    _BesNESlot_Type()
)
besNESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besNESlot.setStatus("mandatory")


class _BesCommonType_Type(DisplayString):
    """Custom type besCommonType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BesCommonType_Type.__name__ = "DisplayString"
_BesCommonType_Object = MibTableColumn
besCommonType = _BesCommonType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 2),
    _BesCommonType_Type()
)
besCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besCommonType.setStatus("mandatory")
_BesCommonDescr_Type = DisplayString
_BesCommonDescr_Object = MibTableColumn
besCommonDescr = _BesCommonDescr_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 3),
    _BesCommonDescr_Type()
)
besCommonDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    besCommonDescr.setStatus("mandatory")


class _BesCommonFirmwareId_Type(DisplayString):
    """Custom type besCommonFirmwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BesCommonFirmwareId_Type.__name__ = "DisplayString"
_BesCommonFirmwareId_Object = MibTableColumn
besCommonFirmwareId = _BesCommonFirmwareId_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 4),
    _BesCommonFirmwareId_Type()
)
besCommonFirmwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besCommonFirmwareId.setStatus("mandatory")
_BesCommonModuleWidth_Type = ModuleWidthValue
_BesCommonModuleWidth_Object = MibTableColumn
besCommonModuleWidth = _BesCommonModuleWidth_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 1, 2, 1, 5),
    _BesCommonModuleWidth_Type()
)
besCommonModuleWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besCommonModuleWidth.setStatus("optional")
_BesStates_ObjectIdentity = ObjectIdentity
besStates = _BesStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2)
)
_BesStatesTable_Object = MibTable
besStatesTable = _BesStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1)
)
if mibBuilder.loadTexts:
    besStatesTable.setStatus("mandatory")
_BesStatesEntry_Object = MibTableRow
besStatesEntry = _BesStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1)
)
besStatesEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besStatesEntry.setStatus("mandatory")
_BesStatesBootloader_Type = PerceivedSeverityValue
_BesStatesBootloader_Object = MibTableColumn
besStatesBootloader = _BesStatesBootloader_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 1),
    _BesStatesBootloader_Type()
)
besStatesBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesBootloader.setStatus("mandatory")
_BesStatesCommLoss_Type = PerceivedSeverityValue
_BesStatesCommLoss_Object = MibTableColumn
besStatesCommLoss = _BesStatesCommLoss_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 2),
    _BesStatesCommLoss_Type()
)
besStatesCommLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesCommLoss.setStatus("mandatory")
_BesStatesTemperatureLow_Type = PerceivedSeverityValue
_BesStatesTemperatureLow_Object = MibTableColumn
besStatesTemperatureLow = _BesStatesTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 3),
    _BesStatesTemperatureLow_Type()
)
besStatesTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesTemperatureLow.setStatus("mandatory")
_BesStatesTemperatureHigh_Type = PerceivedSeverityValue
_BesStatesTemperatureHigh_Object = MibTableColumn
besStatesTemperatureHigh = _BesStatesTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 4),
    _BesStatesTemperatureHigh_Type()
)
besStatesTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesTemperatureHigh.setStatus("mandatory")
_BesStatesInputVoltageLow_Type = PerceivedSeverityValue
_BesStatesInputVoltageLow_Object = MibTableColumn
besStatesInputVoltageLow = _BesStatesInputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 5),
    _BesStatesInputVoltageLow_Type()
)
besStatesInputVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesInputVoltageLow.setStatus("mandatory")
_BesStatesInputVoltageHigh_Type = PerceivedSeverityValue
_BesStatesInputVoltageHigh_Object = MibTableColumn
besStatesInputVoltageHigh = _BesStatesInputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 2, 1, 1, 6),
    _BesStatesInputVoltageHigh_Type()
)
besStatesInputVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besStatesInputVoltageHigh.setStatus("mandatory")
_BesConfiguration_ObjectIdentity = ObjectIdentity
besConfiguration = _BesConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3)
)
_BesConfigurationTable_Object = MibTable
besConfigurationTable = _BesConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1)
)
if mibBuilder.loadTexts:
    besConfigurationTable.setStatus("mandatory")
_BesConfigurationEntry_Object = MibTableRow
besConfigurationEntry = _BesConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1)
)
besConfigurationEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besConfigurationEntry.setStatus("mandatory")
_BesConfigNESlotWrite_Type = NESlotWriteValue
_BesConfigNESlotWrite_Object = MibTableColumn
besConfigNESlotWrite = _BesConfigNESlotWrite_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 1),
    _BesConfigNESlotWrite_Type()
)
besConfigNESlotWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    besConfigNESlotWrite.setStatus("optional")
_BesConfigConfigurationIndex_Type = Integer32
_BesConfigConfigurationIndex_Object = MibTableColumn
besConfigConfigurationIndex = _BesConfigConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 2),
    _BesConfigConfigurationIndex_Type()
)
besConfigConfigurationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    besConfigConfigurationIndex.setStatus("mandatory")
_BesConfigConfiguration_Type = DisplayString
_BesConfigConfiguration_Object = MibTableColumn
besConfigConfiguration = _BesConfigConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 3, 1, 1, 3),
    _BesConfigConfiguration_Type()
)
besConfigConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besConfigConfiguration.setStatus("mandatory")
_BesControl_ObjectIdentity = ObjectIdentity
besControl = _BesControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4)
)
_BesControlTable_Object = MibTable
besControlTable = _BesControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1)
)
if mibBuilder.loadTexts:
    besControlTable.setStatus("mandatory")
_BesControlEntry_Object = MibTableRow
besControlEntry = _BesControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1)
)
besControlEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besControlEntry.setStatus("mandatory")
_BesControlReset_Type = TruthValue
_BesControlReset_Object = MibTableColumn
besControlReset = _BesControlReset_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 1),
    _BesControlReset_Type()
)
besControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    besControlReset.setStatus("mandatory")
_BesControlModuleLedBlink_Type = TruthValue
_BesControlModuleLedBlink_Object = MibTableColumn
besControlModuleLedBlink = _BesControlModuleLedBlink_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 4, 1, 1, 2),
    _BesControlModuleLedBlink_Type()
)
besControlModuleLedBlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    besControlModuleLedBlink.setStatus("mandatory")
_BesMeasuringValues_ObjectIdentity = ObjectIdentity
besMeasuringValues = _BesMeasuringValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5)
)
_BesMeasuringValuesTable_Object = MibTable
besMeasuringValuesTable = _BesMeasuringValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1)
)
if mibBuilder.loadTexts:
    besMeasuringValuesTable.setStatus("mandatory")
_BesMeasuringValuesEntry_Object = MibTableRow
besMeasuringValuesEntry = _BesMeasuringValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1)
)
besMeasuringValuesEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besMeasuringValuesEntry.setStatus("mandatory")
_BesTemperatureLoLo_Type = Integer32
_BesTemperatureLoLo_Object = MibTableColumn
besTemperatureLoLo = _BesTemperatureLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 1),
    _BesTemperatureLoLo_Type()
)
besTemperatureLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTemperatureLoLo.setStatus("mandatory")
_BesTemperatureLo_Type = Integer32
_BesTemperatureLo_Object = MibTableColumn
besTemperatureLo = _BesTemperatureLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 2),
    _BesTemperatureLo_Type()
)
besTemperatureLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTemperatureLo.setStatus("mandatory")
_BesTemperatureValue_Type = Integer32
_BesTemperatureValue_Object = MibTableColumn
besTemperatureValue = _BesTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 3),
    _BesTemperatureValue_Type()
)
besTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTemperatureValue.setStatus("mandatory")
_BesTemperatureHi_Type = Integer32
_BesTemperatureHi_Object = MibTableColumn
besTemperatureHi = _BesTemperatureHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 4),
    _BesTemperatureHi_Type()
)
besTemperatureHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTemperatureHi.setStatus("mandatory")
_BesTemperatureHiHi_Type = Integer32
_BesTemperatureHiHi_Object = MibTableColumn
besTemperatureHiHi = _BesTemperatureHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 5),
    _BesTemperatureHiHi_Type()
)
besTemperatureHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besTemperatureHiHi.setStatus("mandatory")
_BesInputVoltageLoLo_Type = Integer32
_BesInputVoltageLoLo_Object = MibTableColumn
besInputVoltageLoLo = _BesInputVoltageLoLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 6),
    _BesInputVoltageLoLo_Type()
)
besInputVoltageLoLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besInputVoltageLoLo.setStatus("mandatory")
_BesInputVoltageLo_Type = Integer32
_BesInputVoltageLo_Object = MibTableColumn
besInputVoltageLo = _BesInputVoltageLo_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 7),
    _BesInputVoltageLo_Type()
)
besInputVoltageLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besInputVoltageLo.setStatus("mandatory")
_BesInputVoltageValue_Type = Integer32
_BesInputVoltageValue_Object = MibTableColumn
besInputVoltageValue = _BesInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 8),
    _BesInputVoltageValue_Type()
)
besInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besInputVoltageValue.setStatus("mandatory")
_BesInputVoltageHi_Type = Integer32
_BesInputVoltageHi_Object = MibTableColumn
besInputVoltageHi = _BesInputVoltageHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 9),
    _BesInputVoltageHi_Type()
)
besInputVoltageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besInputVoltageHi.setStatus("mandatory")
_BesInputVoltageHiHi_Type = Integer32
_BesInputVoltageHiHi_Object = MibTableColumn
besInputVoltageHiHi = _BesInputVoltageHiHi_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 5, 1, 1, 10),
    _BesInputVoltageHiHi_Type()
)
besInputVoltageHiHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besInputVoltageHiHi.setStatus("mandatory")
_BesDisplay_ObjectIdentity = ObjectIdentity
besDisplay = _BesDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6)
)
_BesDisplayTable_Object = MibTable
besDisplayTable = _BesDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1)
)
if mibBuilder.loadTexts:
    besDisplayTable.setStatus("mandatory")
_BesDisplayEntry_Object = MibTableRow
besDisplayEntry = _BesDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1)
)
besDisplayEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
)
if mibBuilder.loadTexts:
    besDisplayEntry.setStatus("mandatory")
_BesDisplayNumberOfPorts_Type = Integer32
_BesDisplayNumberOfPorts_Object = MibTableColumn
besDisplayNumberOfPorts = _BesDisplayNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 1),
    _BesDisplayNumberOfPorts_Type()
)
besDisplayNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayNumberOfPorts.setStatus("mandatory")
_BesDisplayInputVoltageNominal_Type = Integer32
_BesDisplayInputVoltageNominal_Object = MibTableColumn
besDisplayInputVoltageNominal = _BesDisplayInputVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 2),
    _BesDisplayInputVoltageNominal_Type()
)
besDisplayInputVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayInputVoltageNominal.setStatus("mandatory")
_BesDisplayNumberOfConfigs_Type = Integer32
_BesDisplayNumberOfConfigs_Object = MibTableColumn
besDisplayNumberOfConfigs = _BesDisplayNumberOfConfigs_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 3),
    _BesDisplayNumberOfConfigs_Type()
)
besDisplayNumberOfConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayNumberOfConfigs.setStatus("mandatory")
_BesDisplayConfiguration1_Type = DisplayString
_BesDisplayConfiguration1_Object = MibTableColumn
besDisplayConfiguration1 = _BesDisplayConfiguration1_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 4),
    _BesDisplayConfiguration1_Type()
)
besDisplayConfiguration1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration1.setStatus("mandatory")
_BesDisplayConfiguration2_Type = DisplayString
_BesDisplayConfiguration2_Object = MibTableColumn
besDisplayConfiguration2 = _BesDisplayConfiguration2_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 5),
    _BesDisplayConfiguration2_Type()
)
besDisplayConfiguration2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration2.setStatus("mandatory")
_BesDisplayConfiguration3_Type = DisplayString
_BesDisplayConfiguration3_Object = MibTableColumn
besDisplayConfiguration3 = _BesDisplayConfiguration3_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 6),
    _BesDisplayConfiguration3_Type()
)
besDisplayConfiguration3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration3.setStatus("mandatory")
_BesDisplayConfiguration4_Type = DisplayString
_BesDisplayConfiguration4_Object = MibTableColumn
besDisplayConfiguration4 = _BesDisplayConfiguration4_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 7),
    _BesDisplayConfiguration4_Type()
)
besDisplayConfiguration4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration4.setStatus("mandatory")
_BesDisplayConfiguration5_Type = DisplayString
_BesDisplayConfiguration5_Object = MibTableColumn
besDisplayConfiguration5 = _BesDisplayConfiguration5_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 8),
    _BesDisplayConfiguration5_Type()
)
besDisplayConfiguration5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration5.setStatus("mandatory")
_BesDisplayConfiguration6_Type = DisplayString
_BesDisplayConfiguration6_Object = MibTableColumn
besDisplayConfiguration6 = _BesDisplayConfiguration6_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 9),
    _BesDisplayConfiguration6_Type()
)
besDisplayConfiguration6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration6.setStatus("mandatory")
_BesDisplayConfiguration7_Type = DisplayString
_BesDisplayConfiguration7_Object = MibTableColumn
besDisplayConfiguration7 = _BesDisplayConfiguration7_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 10),
    _BesDisplayConfiguration7_Type()
)
besDisplayConfiguration7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration7.setStatus("mandatory")
_BesDisplayConfiguration8_Type = DisplayString
_BesDisplayConfiguration8_Object = MibTableColumn
besDisplayConfiguration8 = _BesDisplayConfiguration8_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 11),
    _BesDisplayConfiguration8_Type()
)
besDisplayConfiguration8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration8.setStatus("mandatory")
_BesDisplayConfiguration9_Type = DisplayString
_BesDisplayConfiguration9_Object = MibTableColumn
besDisplayConfiguration9 = _BesDisplayConfiguration9_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 12),
    _BesDisplayConfiguration9_Type()
)
besDisplayConfiguration9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration9.setStatus("mandatory")
_BesDisplayConfiguration10_Type = DisplayString
_BesDisplayConfiguration10_Object = MibTableColumn
besDisplayConfiguration10 = _BesDisplayConfiguration10_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 13),
    _BesDisplayConfiguration10_Type()
)
besDisplayConfiguration10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration10.setStatus("mandatory")
_BesDisplayConfiguration11_Type = DisplayString
_BesDisplayConfiguration11_Object = MibTableColumn
besDisplayConfiguration11 = _BesDisplayConfiguration11_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 14),
    _BesDisplayConfiguration11_Type()
)
besDisplayConfiguration11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration11.setStatus("mandatory")
_BesDisplayConfiguration12_Type = DisplayString
_BesDisplayConfiguration12_Object = MibTableColumn
besDisplayConfiguration12 = _BesDisplayConfiguration12_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 15),
    _BesDisplayConfiguration12_Type()
)
besDisplayConfiguration12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration12.setStatus("mandatory")
_BesDisplayConfiguration13_Type = DisplayString
_BesDisplayConfiguration13_Object = MibTableColumn
besDisplayConfiguration13 = _BesDisplayConfiguration13_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 16),
    _BesDisplayConfiguration13_Type()
)
besDisplayConfiguration13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration13.setStatus("mandatory")
_BesDisplayConfiguration14_Type = DisplayString
_BesDisplayConfiguration14_Object = MibTableColumn
besDisplayConfiguration14 = _BesDisplayConfiguration14_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 17),
    _BesDisplayConfiguration14_Type()
)
besDisplayConfiguration14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration14.setStatus("mandatory")
_BesDisplayConfiguration15_Type = DisplayString
_BesDisplayConfiguration15_Object = MibTableColumn
besDisplayConfiguration15 = _BesDisplayConfiguration15_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 18),
    _BesDisplayConfiguration15_Type()
)
besDisplayConfiguration15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration15.setStatus("mandatory")
_BesDisplayConfiguration16_Type = DisplayString
_BesDisplayConfiguration16_Object = MibTableColumn
besDisplayConfiguration16 = _BesDisplayConfiguration16_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 6, 1, 1, 19),
    _BesDisplayConfiguration16_Type()
)
besDisplayConfiguration16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayConfiguration16.setStatus("mandatory")
_BesDisplayPorts_ObjectIdentity = ObjectIdentity
besDisplayPorts = _BesDisplayPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56)
)
_BesDisplayPortsTable_Object = MibTable
besDisplayPortsTable = _BesDisplayPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1)
)
if mibBuilder.loadTexts:
    besDisplayPortsTable.setStatus("mandatory")
_BesDisplayPortsEntry_Object = MibTableRow
besDisplayPortsEntry = _BesDisplayPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1)
)
besDisplayPortsEntry.setIndexNames(
    (0, "BKTEL-HFC862-BES-V01-MIB", "besNESlot"),
    (0, "BKTEL-HFC862-BES-V01-MIB", "besDisplayPortsPortIndex"),
)
if mibBuilder.loadTexts:
    besDisplayPortsEntry.setStatus("mandatory")
_BesDisplayPortsPortIndex_Type = Integer32
_BesDisplayPortsPortIndex_Object = MibTableColumn
besDisplayPortsPortIndex = _BesDisplayPortsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 1),
    _BesDisplayPortsPortIndex_Type()
)
besDisplayPortsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsPortIndex.setStatus("mandatory")
_BesDisplayPortsPortName_Type = DisplayString
_BesDisplayPortsPortName_Object = MibTableColumn
besDisplayPortsPortName = _BesDisplayPortsPortName_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 2),
    _BesDisplayPortsPortName_Type()
)
besDisplayPortsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsPortName.setStatus("mandatory")
_BesDisplayPortsType_Type = PortType
_BesDisplayPortsType_Object = MibTableColumn
besDisplayPortsType = _BesDisplayPortsType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 3),
    _BesDisplayPortsType_Type()
)
besDisplayPortsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsType.setStatus("mandatory")
_BesDisplayPortsLinkState_Type = PortLinkState
_BesDisplayPortsLinkState_Object = MibTableColumn
besDisplayPortsLinkState = _BesDisplayPortsLinkState_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 4),
    _BesDisplayPortsLinkState_Type()
)
besDisplayPortsLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsLinkState.setStatus("mandatory")
_BesDisplayPortsStatus_Type = PortStatus
_BesDisplayPortsStatus_Object = MibTableColumn
besDisplayPortsStatus = _BesDisplayPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 5),
    _BesDisplayPortsStatus_Type()
)
besDisplayPortsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsStatus.setStatus("mandatory")
_BesDisplayPortsDuplexMode_Type = PortDuplexMode
_BesDisplayPortsDuplexMode_Object = MibTableColumn
besDisplayPortsDuplexMode = _BesDisplayPortsDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 6),
    _BesDisplayPortsDuplexMode_Type()
)
besDisplayPortsDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsDuplexMode.setStatus("mandatory")
_BesDisplayPortsSpeed_Type = PortSpeed
_BesDisplayPortsSpeed_Object = MibTableColumn
besDisplayPortsSpeed = _BesDisplayPortsSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 7),
    _BesDisplayPortsSpeed_Type()
)
besDisplayPortsSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsSpeed.setStatus("mandatory")
_BesDisplayPortsFlowControl_Type = PortFlowControl
_BesDisplayPortsFlowControl_Object = MibTableColumn
besDisplayPortsFlowControl = _BesDisplayPortsFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 8),
    _BesDisplayPortsFlowControl_Type()
)
besDisplayPortsFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFlowControl.setStatus("mandatory")
_BesDisplayPortsFiberTxDistance_Type = Integer32
_BesDisplayPortsFiberTxDistance_Object = MibTableColumn
besDisplayPortsFiberTxDistance = _BesDisplayPortsFiberTxDistance_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 9),
    _BesDisplayPortsFiberTxDistance_Type()
)
besDisplayPortsFiberTxDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFiberTxDistance.setStatus("mandatory")
_BesDisplayPortsFiberTxWavelen_Type = Integer32
_BesDisplayPortsFiberTxWavelen_Object = MibTableColumn
besDisplayPortsFiberTxWavelen = _BesDisplayPortsFiberTxWavelen_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 10),
    _BesDisplayPortsFiberTxWavelen_Type()
)
besDisplayPortsFiberTxWavelen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFiberTxWavelen.setStatus("mandatory")
_BesDisplayPortsFiberRxWavelenMin_Type = Integer32
_BesDisplayPortsFiberRxWavelenMin_Object = MibTableColumn
besDisplayPortsFiberRxWavelenMin = _BesDisplayPortsFiberRxWavelenMin_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 11),
    _BesDisplayPortsFiberRxWavelenMin_Type()
)
besDisplayPortsFiberRxWavelenMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFiberRxWavelenMin.setStatus("mandatory")
_BesDisplayPortsFiberRxWavelenMax_Type = Integer32
_BesDisplayPortsFiberRxWavelenMax_Object = MibTableColumn
besDisplayPortsFiberRxWavelenMax = _BesDisplayPortsFiberRxWavelenMax_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 12),
    _BesDisplayPortsFiberRxWavelenMax_Type()
)
besDisplayPortsFiberRxWavelenMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFiberRxWavelenMax.setStatus("mandatory")
_BesDisplayPortsFiberSfpData_Type = DisplayString
_BesDisplayPortsFiberSfpData_Object = MibTableColumn
besDisplayPortsFiberSfpData = _BesDisplayPortsFiberSfpData_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 2, 114, 56, 1, 1, 13),
    _BesDisplayPortsFiberSfpData_Type()
)
besDisplayPortsFiberSfpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    besDisplayPortsFiberSfpData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BKTEL-HFC862-BES-V01-MIB",
    **{"PortType": PortType,
       "PortLinkState": PortLinkState,
       "PortStatus": PortStatus,
       "PortDuplexMode": PortDuplexMode,
       "PortSpeed": PortSpeed,
       "PortFlowControl": PortFlowControl,
       "NESlotWriteValue": NESlotWriteValue,
       "bes": bes,
       "besCommon": besCommon,
       "besCommonNumberOfModules": besCommonNumberOfModules,
       "besCommonTable": besCommonTable,
       "besCommonEntry": besCommonEntry,
       "besNESlot": besNESlot,
       "besCommonType": besCommonType,
       "besCommonDescr": besCommonDescr,
       "besCommonFirmwareId": besCommonFirmwareId,
       "besCommonModuleWidth": besCommonModuleWidth,
       "besStates": besStates,
       "besStatesTable": besStatesTable,
       "besStatesEntry": besStatesEntry,
       "besStatesBootloader": besStatesBootloader,
       "besStatesCommLoss": besStatesCommLoss,
       "besStatesTemperatureLow": besStatesTemperatureLow,
       "besStatesTemperatureHigh": besStatesTemperatureHigh,
       "besStatesInputVoltageLow": besStatesInputVoltageLow,
       "besStatesInputVoltageHigh": besStatesInputVoltageHigh,
       "besConfiguration": besConfiguration,
       "besConfigurationTable": besConfigurationTable,
       "besConfigurationEntry": besConfigurationEntry,
       "besConfigNESlotWrite": besConfigNESlotWrite,
       "besConfigConfigurationIndex": besConfigConfigurationIndex,
       "besConfigConfiguration": besConfigConfiguration,
       "besControl": besControl,
       "besControlTable": besControlTable,
       "besControlEntry": besControlEntry,
       "besControlReset": besControlReset,
       "besControlModuleLedBlink": besControlModuleLedBlink,
       "besMeasuringValues": besMeasuringValues,
       "besMeasuringValuesTable": besMeasuringValuesTable,
       "besMeasuringValuesEntry": besMeasuringValuesEntry,
       "besTemperatureLoLo": besTemperatureLoLo,
       "besTemperatureLo": besTemperatureLo,
       "besTemperatureValue": besTemperatureValue,
       "besTemperatureHi": besTemperatureHi,
       "besTemperatureHiHi": besTemperatureHiHi,
       "besInputVoltageLoLo": besInputVoltageLoLo,
       "besInputVoltageLo": besInputVoltageLo,
       "besInputVoltageValue": besInputVoltageValue,
       "besInputVoltageHi": besInputVoltageHi,
       "besInputVoltageHiHi": besInputVoltageHiHi,
       "besDisplay": besDisplay,
       "besDisplayTable": besDisplayTable,
       "besDisplayEntry": besDisplayEntry,
       "besDisplayNumberOfPorts": besDisplayNumberOfPorts,
       "besDisplayInputVoltageNominal": besDisplayInputVoltageNominal,
       "besDisplayNumberOfConfigs": besDisplayNumberOfConfigs,
       "besDisplayConfiguration1": besDisplayConfiguration1,
       "besDisplayConfiguration2": besDisplayConfiguration2,
       "besDisplayConfiguration3": besDisplayConfiguration3,
       "besDisplayConfiguration4": besDisplayConfiguration4,
       "besDisplayConfiguration5": besDisplayConfiguration5,
       "besDisplayConfiguration6": besDisplayConfiguration6,
       "besDisplayConfiguration7": besDisplayConfiguration7,
       "besDisplayConfiguration8": besDisplayConfiguration8,
       "besDisplayConfiguration9": besDisplayConfiguration9,
       "besDisplayConfiguration10": besDisplayConfiguration10,
       "besDisplayConfiguration11": besDisplayConfiguration11,
       "besDisplayConfiguration12": besDisplayConfiguration12,
       "besDisplayConfiguration13": besDisplayConfiguration13,
       "besDisplayConfiguration14": besDisplayConfiguration14,
       "besDisplayConfiguration15": besDisplayConfiguration15,
       "besDisplayConfiguration16": besDisplayConfiguration16,
       "besDisplayPorts": besDisplayPorts,
       "besDisplayPortsTable": besDisplayPortsTable,
       "besDisplayPortsEntry": besDisplayPortsEntry,
       "besDisplayPortsPortIndex": besDisplayPortsPortIndex,
       "besDisplayPortsPortName": besDisplayPortsPortName,
       "besDisplayPortsType": besDisplayPortsType,
       "besDisplayPortsLinkState": besDisplayPortsLinkState,
       "besDisplayPortsStatus": besDisplayPortsStatus,
       "besDisplayPortsDuplexMode": besDisplayPortsDuplexMode,
       "besDisplayPortsSpeed": besDisplayPortsSpeed,
       "besDisplayPortsFlowControl": besDisplayPortsFlowControl,
       "besDisplayPortsFiberTxDistance": besDisplayPortsFiberTxDistance,
       "besDisplayPortsFiberTxWavelen": besDisplayPortsFiberTxWavelen,
       "besDisplayPortsFiberRxWavelenMin": besDisplayPortsFiberRxWavelenMin,
       "besDisplayPortsFiberRxWavelenMax": besDisplayPortsFiberRxWavelenMax,
       "besDisplayPortsFiberSfpData": besDisplayPortsFiberSfpData}
)
