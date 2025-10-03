# SNMP MIB module (GUDEADS-ESB7214-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gude\GUDEADS-ESB7214-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:02 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsESB7214_ObjectIdentity = ObjectIdentity
gadsESB7214 = _GadsESB7214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67)
)
_Esb7214Objects_ObjectIdentity = ObjectIdentity
esb7214Objects = _Esb7214Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1)
)
_Esb7214CommonConfig_ObjectIdentity = ObjectIdentity
esb7214CommonConfig = _Esb7214CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1)
)
_Esb7214SNMPaccess_ObjectIdentity = ObjectIdentity
esb7214SNMPaccess = _Esb7214SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1)
)


class _Esb7214TrapCtrl_Type(Integer32):
    """Custom type esb7214TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Esb7214TrapCtrl_Type.__name__ = "Integer32"
_Esb7214TrapCtrl_Object = MibScalar
esb7214TrapCtrl = _Esb7214TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1, 1),
    _Esb7214TrapCtrl_Type()
)
esb7214TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214TrapCtrl.setStatus("current")
_Esb7214TrapIPTable_Object = MibTable
esb7214TrapIPTable = _Esb7214TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    esb7214TrapIPTable.setStatus("current")
_Esb7214TrapIPEntry_Object = MibTableRow
esb7214TrapIPEntry = _Esb7214TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1, 2, 1)
)
esb7214TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214TrapIPIndex"),
)
if mibBuilder.loadTexts:
    esb7214TrapIPEntry.setStatus("current")


class _Esb7214TrapIPIndex_Type(Integer32):
    """Custom type esb7214TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Esb7214TrapIPIndex_Type.__name__ = "Integer32"
_Esb7214TrapIPIndex_Object = MibTableColumn
esb7214TrapIPIndex = _Esb7214TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1, 2, 1, 1),
    _Esb7214TrapIPIndex_Type()
)
esb7214TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214TrapIPIndex.setStatus("current")


class _Esb7214TrapAddr_Type(OctetString):
    """Custom type esb7214TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Esb7214TrapAddr_Type.__name__ = "OctetString"
_Esb7214TrapAddr_Object = MibTableColumn
esb7214TrapAddr = _Esb7214TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 1, 1, 2, 1, 2),
    _Esb7214TrapAddr_Type()
)
esb7214TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214TrapAddr.setStatus("current")
_Esb7214DeviceConfig_ObjectIdentity = ObjectIdentity
esb7214DeviceConfig = _Esb7214DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 2)
)
_Esb7214IntActors_ObjectIdentity = ObjectIdentity
esb7214IntActors = _Esb7214IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3)
)
_Esb7214relayports_ObjectIdentity = ObjectIdentity
esb7214relayports = _Esb7214relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1)
)


class _Esb7214portNumber_Type(Integer32):
    """Custom type esb7214portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7214portNumber_Type.__name__ = "Integer32"
_Esb7214portNumber_Object = MibScalar
esb7214portNumber = _Esb7214portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 1),
    _Esb7214portNumber_Type()
)
esb7214portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214portNumber.setStatus("current")
_Esb7214portTable_Object = MibTable
esb7214portTable = _Esb7214portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    esb7214portTable.setStatus("current")
_Esb7214portEntry_Object = MibTableRow
esb7214portEntry = _Esb7214portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1)
)
esb7214portEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214PortIndex"),
)
if mibBuilder.loadTexts:
    esb7214portEntry.setStatus("current")


class _Esb7214PortIndex_Type(Integer32):
    """Custom type esb7214PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7214PortIndex_Type.__name__ = "Integer32"
_Esb7214PortIndex_Object = MibTableColumn
esb7214PortIndex = _Esb7214PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 1),
    _Esb7214PortIndex_Type()
)
esb7214PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214PortIndex.setStatus("current")


class _Esb7214PortName_Type(OctetString):
    """Custom type esb7214PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Esb7214PortName_Type.__name__ = "OctetString"
_Esb7214PortName_Object = MibTableColumn
esb7214PortName = _Esb7214PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 2),
    _Esb7214PortName_Type()
)
esb7214PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortName.setStatus("current")


class _Esb7214PortState_Type(Integer32):
    """Custom type esb7214PortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Esb7214PortState_Type.__name__ = "Integer32"
_Esb7214PortState_Object = MibTableColumn
esb7214PortState = _Esb7214PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 3),
    _Esb7214PortState_Type()
)
esb7214PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortState.setStatus("current")
_Esb7214PortSwitchCount_Type = Integer32
_Esb7214PortSwitchCount_Object = MibTableColumn
esb7214PortSwitchCount = _Esb7214PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 4),
    _Esb7214PortSwitchCount_Type()
)
esb7214PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214PortSwitchCount.setStatus("current")


class _Esb7214PortStartupMode_Type(Integer32):
    """Custom type esb7214PortStartupMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("laststate", 2))
    )


_Esb7214PortStartupMode_Type.__name__ = "Integer32"
_Esb7214PortStartupMode_Object = MibTableColumn
esb7214PortStartupMode = _Esb7214PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 5),
    _Esb7214PortStartupMode_Type()
)
esb7214PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortStartupMode.setStatus("current")


class _Esb7214PortStartupDelay_Type(Integer32):
    """Custom type esb7214PortStartupDelay based on Integer32"""
    defaultValue = 0


_Esb7214PortStartupDelay_Type.__name__ = "Integer32"
_Esb7214PortStartupDelay_Object = MibTableColumn
esb7214PortStartupDelay = _Esb7214PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 6),
    _Esb7214PortStartupDelay_Type()
)
esb7214PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    esb7214PortStartupDelay.setUnits("seconds")


class _Esb7214PortRepowerTime_Type(Integer32):
    """Custom type esb7214PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Esb7214PortRepowerTime_Type.__name__ = "Integer32"
_Esb7214PortRepowerTime_Object = MibTableColumn
esb7214PortRepowerTime = _Esb7214PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 7),
    _Esb7214PortRepowerTime_Type()
)
esb7214PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    esb7214PortRepowerTime.setUnits("seconds")


class _Esb7214PortResetDuration_Type(Integer32):
    """Custom type esb7214PortResetDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Esb7214PortResetDuration_Type.__name__ = "Integer32"
_Esb7214PortResetDuration_Object = MibTableColumn
esb7214PortResetDuration = _Esb7214PortResetDuration_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 3, 1, 2, 1, 8),
    _Esb7214PortResetDuration_Type()
)
esb7214PortResetDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214PortResetDuration.setStatus("current")
if mibBuilder.loadTexts:
    esb7214PortResetDuration.setUnits("seconds")
_Esb7214ExtActors_ObjectIdentity = ObjectIdentity
esb7214ExtActors = _Esb7214ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 4)
)
_Esb7214IntSensors_ObjectIdentity = ObjectIdentity
esb7214IntSensors = _Esb7214IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5)
)
_Esb7214Inputs_ObjectIdentity = ObjectIdentity
esb7214Inputs = _Esb7214Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6)
)


class _Esb7214ActiveInputs_Type(Unsigned32):
    """Custom type esb7214ActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7214ActiveInputs_Type.__name__ = "Unsigned32"
_Esb7214ActiveInputs_Object = MibScalar
esb7214ActiveInputs = _Esb7214ActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 1),
    _Esb7214ActiveInputs_Type()
)
esb7214ActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ActiveInputs.setStatus("current")
_Esb7214InputTable_Object = MibTable
esb7214InputTable = _Esb7214InputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    esb7214InputTable.setStatus("current")
_Esb7214InputEntry_Object = MibTableRow
esb7214InputEntry = _Esb7214InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 2, 1)
)
esb7214InputEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214InputIndex"),
)
if mibBuilder.loadTexts:
    esb7214InputEntry.setStatus("current")


class _Esb7214InputIndex_Type(Integer32):
    """Custom type esb7214InputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7214InputIndex_Type.__name__ = "Integer32"
_Esb7214InputIndex_Object = MibTableColumn
esb7214InputIndex = _Esb7214InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 2, 1, 1),
    _Esb7214InputIndex_Type()
)
esb7214InputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214InputIndex.setStatus("current")


class _Esb7214Input_Type(Integer32):
    """Custom type esb7214Input based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lo", 0),
          ("hi", 1))
    )


_Esb7214Input_Type.__name__ = "Integer32"
_Esb7214Input_Object = MibTableColumn
esb7214Input = _Esb7214Input_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 2, 1, 2),
    _Esb7214Input_Type()
)
esb7214Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214Input.setStatus("current")


class _Esb7214InputName_Type(OctetString):
    """Custom type esb7214InputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Esb7214InputName_Type.__name__ = "OctetString"
_Esb7214InputName_Object = MibTableColumn
esb7214InputName = _Esb7214InputName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 6, 2, 1, 32),
    _Esb7214InputName_Type()
)
esb7214InputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214InputName.setStatus("current")


class _Esb7214POE_Type(Integer32):
    """Custom type esb7214POE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Esb7214POE_Type.__name__ = "Integer32"
_Esb7214POE_Object = MibScalar
esb7214POE = _Esb7214POE_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 10),
    _Esb7214POE_Type()
)
esb7214POE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214POE.setStatus("current")
if mibBuilder.loadTexts:
    esb7214POE.setUnits("0 = no POE, 1 = POE available")
_Esb7214PwrSupplyTable_Object = MibTable
esb7214PwrSupplyTable = _Esb7214PwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 13)
)
if mibBuilder.loadTexts:
    esb7214PwrSupplyTable.setStatus("current")
_Esb7214PwrSupplyEntry_Object = MibTableRow
esb7214PwrSupplyEntry = _Esb7214PwrSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 13, 1)
)
esb7214PwrSupplyEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214PwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    esb7214PwrSupplyEntry.setStatus("current")


class _Esb7214PwrSupplyIndex_Type(Integer32):
    """Custom type esb7214PwrSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Esb7214PwrSupplyIndex_Type.__name__ = "Integer32"
_Esb7214PwrSupplyIndex_Object = MibTableColumn
esb7214PwrSupplyIndex = _Esb7214PwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 13, 1, 1),
    _Esb7214PwrSupplyIndex_Type()
)
esb7214PwrSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214PwrSupplyIndex.setStatus("current")


class _Esb7214PwrSupplyStatus_Type(Integer32):
    """Custom type esb7214PwrSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_Esb7214PwrSupplyStatus_Type.__name__ = "Integer32"
_Esb7214PwrSupplyStatus_Object = MibTableColumn
esb7214PwrSupplyStatus = _Esb7214PwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 13, 1, 2),
    _Esb7214PwrSupplyStatus_Type()
)
esb7214PwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214PwrSupplyStatus.setStatus("current")
_Esb7214NTPClient_ObjectIdentity = ObjectIdentity
esb7214NTPClient = _Esb7214NTPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 15)
)


class _Esb7214NTPTimeValid_Type(Integer32):
    """Custom type esb7214NTPTimeValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notime", 0),
          ("valid", 1))
    )


_Esb7214NTPTimeValid_Type.__name__ = "Integer32"
_Esb7214NTPTimeValid_Object = MibScalar
esb7214NTPTimeValid = _Esb7214NTPTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 15, 1),
    _Esb7214NTPTimeValid_Type()
)
esb7214NTPTimeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214NTPTimeValid.setStatus("current")
_Esb7214NTPUnixTime_Type = Unsigned32
_Esb7214NTPUnixTime_Object = MibScalar
esb7214NTPUnixTime = _Esb7214NTPUnixTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 15, 2),
    _Esb7214NTPUnixTime_Type()
)
esb7214NTPUnixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214NTPUnixTime.setStatus("current")
if mibBuilder.loadTexts:
    esb7214NTPUnixTime.setUnits("s")
_Esb7214NTPLastValidTimestamp_Type = Unsigned32
_Esb7214NTPLastValidTimestamp_Object = MibScalar
esb7214NTPLastValidTimestamp = _Esb7214NTPLastValidTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 5, 15, 3),
    _Esb7214NTPLastValidTimestamp_Type()
)
esb7214NTPLastValidTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214NTPLastValidTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    esb7214NTPLastValidTimestamp.setUnits("s")
_Esb7214ExtSensors_ObjectIdentity = ObjectIdentity
esb7214ExtSensors = _Esb7214ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6)
)
_Esb7214SensorTable_Object = MibTable
esb7214SensorTable = _Esb7214SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1)
)
if mibBuilder.loadTexts:
    esb7214SensorTable.setStatus("current")
_Esb7214SensorEntry_Object = MibTableRow
esb7214SensorEntry = _Esb7214SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1)
)
esb7214SensorEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
)
if mibBuilder.loadTexts:
    esb7214SensorEntry.setStatus("current")


class _Esb7214SensorIndex_Type(Integer32):
    """Custom type esb7214SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Esb7214SensorIndex_Type.__name__ = "Integer32"
_Esb7214SensorIndex_Object = MibTableColumn
esb7214SensorIndex = _Esb7214SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 1),
    _Esb7214SensorIndex_Type()
)
esb7214SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214SensorIndex.setStatus("current")
_Esb7214TempSensor_Type = Integer32
_Esb7214TempSensor_Object = MibTableColumn
esb7214TempSensor = _Esb7214TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 2),
    _Esb7214TempSensor_Type()
)
esb7214TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    esb7214TempSensor.setUnits("0.1 degree Celsius")
_Esb7214HygroSensor_Type = Integer32
_Esb7214HygroSensor_Object = MibTableColumn
esb7214HygroSensor = _Esb7214HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 3),
    _Esb7214HygroSensor_Type()
)
esb7214HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    esb7214HygroSensor.setUnits("0.1 percent humidity")


class _Esb7214InputSensor_Type(Integer32):
    """Custom type esb7214InputSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Esb7214InputSensor_Type.__name__ = "Integer32"
_Esb7214InputSensor_Object = MibTableColumn
esb7214InputSensor = _Esb7214InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 4),
    _Esb7214InputSensor_Type()
)
esb7214InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214InputSensor.setStatus("current")
_Esb7214AirPressure_Type = Integer32
_Esb7214AirPressure_Object = MibTableColumn
esb7214AirPressure = _Esb7214AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 5),
    _Esb7214AirPressure_Type()
)
esb7214AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    esb7214AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Esb7214DewPoint_Type = Integer32
_Esb7214DewPoint_Object = MibTableColumn
esb7214DewPoint = _Esb7214DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 6),
    _Esb7214DewPoint_Type()
)
esb7214DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    esb7214DewPoint.setUnits("0.1 degree Celsius")
_Esb7214DewPointDiff_Type = Integer32
_Esb7214DewPointDiff_Object = MibTableColumn
esb7214DewPointDiff = _Esb7214DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 7),
    _Esb7214DewPointDiff_Type()
)
esb7214DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    esb7214DewPointDiff.setUnits("0.1 degree Celsius")


class _Esb7214ExtSensorName_Type(OctetString):
    """Custom type esb7214ExtSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Esb7214ExtSensorName_Type.__name__ = "OctetString"
_Esb7214ExtSensorName_Object = MibTableColumn
esb7214ExtSensorName = _Esb7214ExtSensorName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 1, 1, 32),
    _Esb7214ExtSensorName_Type()
)
esb7214ExtSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214ExtSensorName.setStatus("current")
_Esb7214ExtInputs_ObjectIdentity = ObjectIdentity
esb7214ExtInputs = _Esb7214ExtInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2)
)


class _Esb7214ExtActiveInputs_Type(Unsigned32):
    """Custom type esb7214ExtActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7214ExtActiveInputs_Type.__name__ = "Unsigned32"
_Esb7214ExtActiveInputs_Object = MibScalar
esb7214ExtActiveInputs = _Esb7214ExtActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 1),
    _Esb7214ExtActiveInputs_Type()
)
esb7214ExtActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ExtActiveInputs.setStatus("current")
_Esb7214ExtInputTable_Object = MibTable
esb7214ExtInputTable = _Esb7214ExtInputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    esb7214ExtInputTable.setStatus("current")
_Esb7214ExtInputEntry_Object = MibTableRow
esb7214ExtInputEntry = _Esb7214ExtInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1)
)
esb7214ExtInputEntry.setIndexNames(
    (0, "GUDEADS-ESB7214-MIB", "esb7214ExtInputIndex"),
)
if mibBuilder.loadTexts:
    esb7214ExtInputEntry.setStatus("current")
_Esb7214ExtInputIndex_Type = Unsigned32
_Esb7214ExtInputIndex_Object = MibTableColumn
esb7214ExtInputIndex = _Esb7214ExtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1, 1),
    _Esb7214ExtInputIndex_Type()
)
esb7214ExtInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ExtInputIndex.setStatus("current")


class _Esb7214ExtInput_Type(Integer32):
    """Custom type esb7214ExtInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lo", 0),
          ("hi", 1))
    )


_Esb7214ExtInput_Type.__name__ = "Integer32"
_Esb7214ExtInput_Object = MibTableColumn
esb7214ExtInput = _Esb7214ExtInput_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1, 2),
    _Esb7214ExtInput_Type()
)
esb7214ExtInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ExtInput.setStatus("current")


class _Esb7214ExtInputName_Type(OctetString):
    """Custom type esb7214ExtInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Esb7214ExtInputName_Type.__name__ = "OctetString"
_Esb7214ExtInputName_Object = MibTableColumn
esb7214ExtInputName = _Esb7214ExtInputName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1, 32),
    _Esb7214ExtInputName_Type()
)
esb7214ExtInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7214ExtInputName.setStatus("current")
_Esb7214ExtInputPortNum_Type = Integer32
_Esb7214ExtInputPortNum_Object = MibTableColumn
esb7214ExtInputPortNum = _Esb7214ExtInputPortNum_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1, 33),
    _Esb7214ExtInputPortNum_Type()
)
esb7214ExtInputPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ExtInputPortNum.setStatus("current")
_Esb7214ExtInputBlockIndex_Type = Integer32
_Esb7214ExtInputBlockIndex_Object = MibTableColumn
esb7214ExtInputBlockIndex = _Esb7214ExtInputBlockIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 67, 1, 6, 2, 2, 1, 34),
    _Esb7214ExtInputBlockIndex_Type()
)
esb7214ExtInputBlockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7214ExtInputBlockIndex.setStatus("current")
_Esb7214Conf_ObjectIdentity = ObjectIdentity
esb7214Conf = _Esb7214Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 2)
)
_Esb7214Groups_ObjectIdentity = ObjectIdentity
esb7214Groups = _Esb7214Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 2, 1)
)
_Esb7214Compls_ObjectIdentity = ObjectIdentity
esb7214Compls = _Esb7214Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3)
)

# Managed Objects groups

esb7214BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 67, 2, 1, 1)
)
esb7214BasicGroup.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214TrapCtrl"),
        ("GUDEADS-ESB7214-MIB", "esb7214TrapIPIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214TrapAddr"),
        ("GUDEADS-ESB7214-MIB", "esb7214portNumber"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortName"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortState"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortSwitchCount"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortStartupMode"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortStartupDelay"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortRepowerTime"),
        ("GUDEADS-ESB7214-MIB", "esb7214ActiveInputs"),
        ("GUDEADS-ESB7214-MIB", "esb7214InputIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214Input"),
        ("GUDEADS-ESB7214-MIB", "esb7214POE"),
        ("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214TempSensor"),
        ("GUDEADS-ESB7214-MIB", "esb7214HygroSensor"),
        ("GUDEADS-ESB7214-MIB", "esb7214InputSensor"),
        ("GUDEADS-ESB7214-MIB", "esb7214AirPressure"),
        ("GUDEADS-ESB7214-MIB", "esb7214DewPoint"),
        ("GUDEADS-ESB7214-MIB", "esb7214DewPointDiff"),
        ("GUDEADS-ESB7214-MIB", "esb7214PwrSupplyIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214PwrSupplyStatus"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtSensorName"),
        ("GUDEADS-ESB7214-MIB", "esb7214InputName"),
        ("GUDEADS-ESB7214-MIB", "esb7214NTPTimeValid"),
        ("GUDEADS-ESB7214-MIB", "esb7214NTPUnixTime"),
        ("GUDEADS-ESB7214-MIB", "esb7214NTPLastValidTimestamp"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortResetDuration"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtActiveInputs"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInput"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputName"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputPortNum"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputBlockIndex"))
)
if mibBuilder.loadTexts:
    esb7214BasicGroup.setStatus("current")


# Notification objects

esb7214SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 1)
)
esb7214SwitchEvtPort.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214PortIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortName"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortState"),
        ("GUDEADS-ESB7214-MIB", "esb7214PortSwitchCount"))
)
if mibBuilder.loadTexts:
    esb7214SwitchEvtPort.setStatus(
        "current"
    )

esb7214InputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 2)
)
esb7214InputEvt.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214InputIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214Input"))
)
if mibBuilder.loadTexts:
    esb7214InputEvt.setStatus(
        "current"
    )

esb7214TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 3)
)
esb7214TempEvtSen.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214TempSensor"))
)
if mibBuilder.loadTexts:
    esb7214TempEvtSen.setStatus(
        "current"
    )

esb7214HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 4)
)
esb7214HygroEvtSen.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214HygroSensor"))
)
if mibBuilder.loadTexts:
    esb7214HygroEvtSen.setStatus(
        "current"
    )

esb7214InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 5)
)
esb7214InputEvtSen.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214InputSensor"))
)
if mibBuilder.loadTexts:
    esb7214InputEvtSen.setStatus(
        "current"
    )

esb7214AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 6)
)
esb7214AirPressureEvtSen.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214AirPressure"))
)
if mibBuilder.loadTexts:
    esb7214AirPressureEvtSen.setStatus(
        "current"
    )

esb7214DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 7)
)
esb7214DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214SensorIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214DewPointDiff"))
)
if mibBuilder.loadTexts:
    esb7214DewPtDiffEvtSen.setStatus(
        "current"
    )

esb7214POEEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 8)
)
esb7214POEEvt.setObjects(
    ("GUDEADS-ESB7214-MIB", "esb7214POE")
)
if mibBuilder.loadTexts:
    esb7214POEEvt.setStatus(
        "current"
    )

esb7214PwrSupplyChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 9)
)
esb7214PwrSupplyChangeEvt.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214PwrSupplyIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214PwrSupplyStatus"))
)
if mibBuilder.loadTexts:
    esb7214PwrSupplyChangeEvt.setStatus(
        "current"
    )

esb7214ExtInputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 67, 3, 25)
)
esb7214ExtInputEvt.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214ExtInputIndex"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInput"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputName"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputPortNum"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputBlockIndex"))
)
if mibBuilder.loadTexts:
    esb7214ExtInputEvt.setStatus(
        "current"
    )


# Notifications groups

esb7214NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 67, 2, 1, 2)
)
esb7214NotificationGroup.setObjects(
      *(("GUDEADS-ESB7214-MIB", "esb7214InputEvt"),
        ("GUDEADS-ESB7214-MIB", "esb7214TempEvtSen"),
        ("GUDEADS-ESB7214-MIB", "esb7214HygroEvtSen"),
        ("GUDEADS-ESB7214-MIB", "esb7214InputEvtSen"),
        ("GUDEADS-ESB7214-MIB", "esb7214AirPressureEvtSen"),
        ("GUDEADS-ESB7214-MIB", "esb7214DewPtDiffEvtSen"),
        ("GUDEADS-ESB7214-MIB", "esb7214POEEvt"),
        ("GUDEADS-ESB7214-MIB", "esb7214SwitchEvtPort"),
        ("GUDEADS-ESB7214-MIB", "esb7214PwrSupplyChangeEvt"),
        ("GUDEADS-ESB7214-MIB", "esb7214ExtInputEvt"))
)
if mibBuilder.loadTexts:
    esb7214NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ESB7214-MIB",
    **{"gudeads": gudeads,
       "gadsESB7214": gadsESB7214,
       "esb7214Objects": esb7214Objects,
       "esb7214CommonConfig": esb7214CommonConfig,
       "esb7214SNMPaccess": esb7214SNMPaccess,
       "esb7214TrapCtrl": esb7214TrapCtrl,
       "esb7214TrapIPTable": esb7214TrapIPTable,
       "esb7214TrapIPEntry": esb7214TrapIPEntry,
       "esb7214TrapIPIndex": esb7214TrapIPIndex,
       "esb7214TrapAddr": esb7214TrapAddr,
       "esb7214DeviceConfig": esb7214DeviceConfig,
       "esb7214IntActors": esb7214IntActors,
       "esb7214relayports": esb7214relayports,
       "esb7214portNumber": esb7214portNumber,
       "esb7214portTable": esb7214portTable,
       "esb7214portEntry": esb7214portEntry,
       "esb7214PortIndex": esb7214PortIndex,
       "esb7214PortName": esb7214PortName,
       "esb7214PortState": esb7214PortState,
       "esb7214PortSwitchCount": esb7214PortSwitchCount,
       "esb7214PortStartupMode": esb7214PortStartupMode,
       "esb7214PortStartupDelay": esb7214PortStartupDelay,
       "esb7214PortRepowerTime": esb7214PortRepowerTime,
       "esb7214PortResetDuration": esb7214PortResetDuration,
       "esb7214ExtActors": esb7214ExtActors,
       "esb7214IntSensors": esb7214IntSensors,
       "esb7214Inputs": esb7214Inputs,
       "esb7214ActiveInputs": esb7214ActiveInputs,
       "esb7214InputTable": esb7214InputTable,
       "esb7214InputEntry": esb7214InputEntry,
       "esb7214InputIndex": esb7214InputIndex,
       "esb7214Input": esb7214Input,
       "esb7214InputName": esb7214InputName,
       "esb7214POE": esb7214POE,
       "esb7214PwrSupplyTable": esb7214PwrSupplyTable,
       "esb7214PwrSupplyEntry": esb7214PwrSupplyEntry,
       "esb7214PwrSupplyIndex": esb7214PwrSupplyIndex,
       "esb7214PwrSupplyStatus": esb7214PwrSupplyStatus,
       "esb7214NTPClient": esb7214NTPClient,
       "esb7214NTPTimeValid": esb7214NTPTimeValid,
       "esb7214NTPUnixTime": esb7214NTPUnixTime,
       "esb7214NTPLastValidTimestamp": esb7214NTPLastValidTimestamp,
       "esb7214ExtSensors": esb7214ExtSensors,
       "esb7214SensorTable": esb7214SensorTable,
       "esb7214SensorEntry": esb7214SensorEntry,
       "esb7214SensorIndex": esb7214SensorIndex,
       "esb7214TempSensor": esb7214TempSensor,
       "esb7214HygroSensor": esb7214HygroSensor,
       "esb7214InputSensor": esb7214InputSensor,
       "esb7214AirPressure": esb7214AirPressure,
       "esb7214DewPoint": esb7214DewPoint,
       "esb7214DewPointDiff": esb7214DewPointDiff,
       "esb7214ExtSensorName": esb7214ExtSensorName,
       "esb7214ExtInputs": esb7214ExtInputs,
       "esb7214ExtActiveInputs": esb7214ExtActiveInputs,
       "esb7214ExtInputTable": esb7214ExtInputTable,
       "esb7214ExtInputEntry": esb7214ExtInputEntry,
       "esb7214ExtInputIndex": esb7214ExtInputIndex,
       "esb7214ExtInput": esb7214ExtInput,
       "esb7214ExtInputName": esb7214ExtInputName,
       "esb7214ExtInputPortNum": esb7214ExtInputPortNum,
       "esb7214ExtInputBlockIndex": esb7214ExtInputBlockIndex,
       "esb7214Conf": esb7214Conf,
       "esb7214Groups": esb7214Groups,
       "esb7214BasicGroup": esb7214BasicGroup,
       "esb7214NotificationGroup": esb7214NotificationGroup,
       "esb7214Compls": esb7214Compls,
       "events": events,
       "esb7214SwitchEvtPort": esb7214SwitchEvtPort,
       "esb7214InputEvt": esb7214InputEvt,
       "esb7214TempEvtSen": esb7214TempEvtSen,
       "esb7214HygroEvtSen": esb7214HygroEvtSen,
       "esb7214InputEvtSen": esb7214InputEvtSen,
       "esb7214AirPressureEvtSen": esb7214AirPressureEvtSen,
       "esb7214DewPtDiffEvtSen": esb7214DewPtDiffEvtSen,
       "esb7214POEEvt": esb7214POEEvt,
       "esb7214PwrSupplyChangeEvt": esb7214PwrSupplyChangeEvt,
       "esb7214ExtInputEvt": esb7214ExtInputEvt}
)
