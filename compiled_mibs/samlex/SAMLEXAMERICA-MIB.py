# SNMP MIB module (SAMLEXAMERICA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\samlex\SAMLEXAMERICA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:01 2025
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

samlexamericaInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1)
)
if mibBuilder.loadTexts:
    samlexamericaInfo.setRevisions(
        ("2016-12-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Samlexamerica_ObjectIdentity = ObjectIdentity
samlexamerica = _Samlexamerica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 1)
)
_Model_Type = DisplayString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 1, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("current")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1, 1)
)
trapEntry.setIndexNames(
    (0, "SAMLEXAMERICA-MIB", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("current")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("current")


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibTableColumn
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1, 1, 2),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("current")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1, 1, 3),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 2, 1, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")
_Telecom_ObjectIdentity = ObjectIdentity
telecom = _Telecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3)
)
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1)
)


class _CfgVout_Type(Integer32):
    """Custom type cfgVout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgVout_Type.__name__ = "Integer32"
_CfgVout_Object = MibScalar
cfgVout = _CfgVout_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 1),
    _CfgVout_Type()
)
cfgVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgVout.setStatus("current")


class _Vout_Type(Integer32):
    """Custom type vout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Vout_Type.__name__ = "Integer32"
_Vout_Object = MibScalar
vout = _Vout_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 2),
    _Vout_Type()
)
vout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vout.setStatus("current")


class _Iout_Type(Integer32):
    """Custom type iout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Iout_Type.__name__ = "Integer32"
_Iout_Object = MibScalar
iout = _Iout_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 3),
    _Iout_Type()
)
iout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iout.setStatus("current")


class _Power_Type(Integer32):
    """Custom type power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Power_Type.__name__ = "Integer32"
_Power_Object = MibScalar
power = _Power_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 4),
    _Power_Type()
)
power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power.setStatus("current")


class _CfgFrequency_Type(Integer32):
    """Custom type cfgFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgFrequency_Type.__name__ = "Integer32"
_CfgFrequency_Object = MibScalar
cfgFrequency = _CfgFrequency_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 5),
    _CfgFrequency_Type()
)
cfgFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgFrequency.setStatus("current")


class _Frequency_Type(Integer32):
    """Custom type frequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Frequency_Type.__name__ = "Integer32"
_Frequency_Object = MibScalar
frequency = _Frequency_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 6),
    _Frequency_Type()
)
frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequency.setStatus("current")


class _Gridvout_Type(Integer32):
    """Custom type gridvout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gridvout_Type.__name__ = "Integer32"
_Gridvout_Object = MibScalar
gridvout = _Gridvout_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 7),
    _Gridvout_Type()
)
gridvout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridvout.setStatus("current")


class _Gridiout_Type(Integer32):
    """Custom type gridiout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gridiout_Type.__name__ = "Integer32"
_Gridiout_Object = MibScalar
gridiout = _Gridiout_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 8),
    _Gridiout_Type()
)
gridiout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridiout.setStatus("current")


class _Gridpower_Type(Integer32):
    """Custom type gridpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gridpower_Type.__name__ = "Integer32"
_Gridpower_Object = MibScalar
gridpower = _Gridpower_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 9),
    _Gridpower_Type()
)
gridpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridpower.setStatus("current")


class _Gridfrequency_Type(Integer32):
    """Custom type gridfrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gridfrequency_Type.__name__ = "Integer32"
_Gridfrequency_Object = MibScalar
gridfrequency = _Gridfrequency_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 1, 10),
    _Gridfrequency_Type()
)
gridfrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridfrequency.setStatus("current")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2)
)


class _Vin_Type(Integer32):
    """Custom type vin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Vin_Type.__name__ = "Integer32"
_Vin_Object = MibScalar
vin = _Vin_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 1),
    _Vin_Type()
)
vin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vin.setStatus("current")


class _Ovp_Type(Integer32):
    """Custom type ovp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ovp_Type.__name__ = "Integer32"
_Ovp_Object = MibScalar
ovp = _Ovp_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 2),
    _Ovp_Type()
)
ovp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovp.setStatus("current")


class _OvpRecovery_Type(Integer32):
    """Custom type ovpRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OvpRecovery_Type.__name__ = "Integer32"
_OvpRecovery_Object = MibScalar
ovpRecovery = _OvpRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 3),
    _OvpRecovery_Type()
)
ovpRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovpRecovery.setStatus("current")


class _Uvp_Type(Integer32):
    """Custom type uvp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Uvp_Type.__name__ = "Integer32"
_Uvp_Object = MibScalar
uvp = _Uvp_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 4),
    _Uvp_Type()
)
uvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uvp.setStatus("current")


class _UvpRecovery_Type(Integer32):
    """Custom type uvpRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UvpRecovery_Type.__name__ = "Integer32"
_UvpRecovery_Object = MibScalar
uvpRecovery = _UvpRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 5),
    _UvpRecovery_Type()
)
uvpRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uvpRecovery.setStatus("current")


class _OvAlarm_Type(Integer32):
    """Custom type ovAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OvAlarm_Type.__name__ = "Integer32"
_OvAlarm_Object = MibScalar
ovAlarm = _OvAlarm_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 6),
    _OvAlarm_Type()
)
ovAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ovAlarm.setStatus("current")


class _UvAlarm_Type(Integer32):
    """Custom type uvAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UvAlarm_Type.__name__ = "Integer32"
_UvAlarm_Object = MibScalar
uvAlarm = _UvAlarm_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 2, 7),
    _UvAlarm_Type()
)
uvAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uvAlarm.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3)
)


class _Fan_Type(Integer32):
    """Custom type fan based on Integer32"""
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


_Fan_Type.__name__ = "Integer32"
_Fan_Object = MibScalar
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 1),
    _Fan_Type()
)
fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan.setStatus("current")


class _InverterMode_Type(Integer32):
    """Custom type inverterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off-Line", 0),
          ("on-Line", 1))
    )


_InverterMode_Type.__name__ = "Integer32"
_InverterMode_Object = MibScalar
inverterMode = _InverterMode_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 2),
    _InverterMode_Type()
)
inverterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterMode.setStatus("current")


class _TransferType_Type(Integer32):
    """Custom type transferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 0),
          ("unsynchronized", 1))
    )


_TransferType_Type.__name__ = "Integer32"
_TransferType_Object = MibScalar
transferType = _TransferType_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 3),
    _TransferType_Type()
)
transferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferType.setStatus("current")


class _ByPassRelay_Type(Integer32):
    """Custom type byPassRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("grid", 0),
          ("inverter", 1))
    )


_ByPassRelay_Type.__name__ = "Integer32"
_ByPassRelay_Object = MibScalar
byPassRelay = _ByPassRelay_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 4),
    _ByPassRelay_Type()
)
byPassRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byPassRelay.setStatus("current")


class _GridAC_Type(Integer32):
    """Custom type gridAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-exists", 0),
          ("detect", 1),
          ("present", 2),
          ("sync", 3),
          ("wont-sync", 4))
    )


_GridAC_Type.__name__ = "Integer32"
_GridAC_Object = MibScalar
gridAC = _GridAC_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 5),
    _GridAC_Type()
)
gridAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridAC.setStatus("current")


class _OlProtection_Type(Integer32):
    """Custom type olProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OlProtection_Type.__name__ = "Integer32"
_OlProtection_Object = MibScalar
olProtection = _OlProtection_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 6),
    _OlProtection_Type()
)
olProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olProtection.setStatus("current")


class _SyncFreq_Type(Integer32):
    """Custom type syncFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SyncFreq_Type.__name__ = "Integer32"
_SyncFreq_Object = MibScalar
syncFreq = _SyncFreq_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 7),
    _SyncFreq_Type()
)
syncFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncFreq.setStatus("current")


class _TempDD_Type(Integer32):
    """Custom type tempDD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempDD_Type.__name__ = "Integer32"
_TempDD_Object = MibScalar
tempDD = _TempDD_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 8),
    _TempDD_Type()
)
tempDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDD.setStatus("current")


class _TempDA_Type(Integer32):
    """Custom type tempDA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempDA_Type.__name__ = "Integer32"
_TempDA_Object = MibScalar
tempDA = _TempDA_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 3, 9),
    _TempDA_Type()
)
tempDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDA.setStatus("current")
_Ui_ObjectIdentity = ObjectIdentity
ui = _Ui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 4)
)


class _LcdContrast_Type(Integer32):
    """Custom type lcdContrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcdContrast_Type.__name__ = "Integer32"
_LcdContrast_Object = MibScalar
lcdContrast = _LcdContrast_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 4, 1),
    _LcdContrast_Type()
)
lcdContrast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdContrast.setStatus("current")


class _LcdAutoOff_Type(Integer32):
    """Custom type lcdAutoOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcdAutoOff_Type.__name__ = "Integer32"
_LcdAutoOff_Object = MibScalar
lcdAutoOff = _LcdAutoOff_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 4, 2),
    _LcdAutoOff_Type()
)
lcdAutoOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdAutoOff.setStatus("current")


class _Rs232Speed_Type(Integer32):
    """Custom type rs232Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rs232Speed_Type.__name__ = "Integer32"
_Rs232Speed_Object = MibScalar
rs232Speed = _Rs232Speed_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 4, 3),
    _Rs232Speed_Type()
)
rs232Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232Speed.setStatus("current")


class _UsbVCOMSpeed_Type(Integer32):
    """Custom type usbVCOMSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsbVCOMSpeed_Type.__name__ = "Integer32"
_UsbVCOMSpeed_Object = MibScalar
usbVCOMSpeed = _UsbVCOMSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 4, 4),
    _UsbVCOMSpeed_Type()
)
usbVCOMSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbVCOMSpeed.setStatus("current")
_Warningconfig_ObjectIdentity = ObjectIdentity
warningconfig = _Warningconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5)
)
_WcTable_Object = MibTable
wcTable = _WcTable_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    wcTable.setStatus("current")
_WcEntry_Object = MibTableRow
wcEntry = _WcEntry_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1)
)
wcEntry.setIndexNames(
    (0, "SAMLEXAMERICA-MIB", "wcIndex"),
)
if mibBuilder.loadTexts:
    wcEntry.setStatus("current")


class _WcIndex_Type(Integer32):
    """Custom type wcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("buzzer", 0),
          ("drycontact", 1))
    )


_WcIndex_Type.__name__ = "Integer32"
_WcIndex_Object = MibTableColumn
wcIndex = _WcIndex_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 1),
    _WcIndex_Type()
)
wcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wcIndex.setStatus("current")


class _WcFanFaultEnabled_Type(Integer32):
    """Custom type wcFanFaultEnabled based on Integer32"""
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


_WcFanFaultEnabled_Type.__name__ = "Integer32"
_WcFanFaultEnabled_Object = MibTableColumn
wcFanFaultEnabled = _WcFanFaultEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 2),
    _WcFanFaultEnabled_Type()
)
wcFanFaultEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcFanFaultEnabled.setStatus("current")


class _WcOVAEnabled_Type(Integer32):
    """Custom type wcOVAEnabled based on Integer32"""
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


_WcOVAEnabled_Type.__name__ = "Integer32"
_WcOVAEnabled_Object = MibTableColumn
wcOVAEnabled = _WcOVAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 3),
    _WcOVAEnabled_Type()
)
wcOVAEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcOVAEnabled.setStatus("current")


class _WcUVAEnabled_Type(Integer32):
    """Custom type wcUVAEnabled based on Integer32"""
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


_WcUVAEnabled_Type.__name__ = "Integer32"
_WcUVAEnabled_Object = MibTableColumn
wcUVAEnabled = _WcUVAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 4),
    _WcUVAEnabled_Type()
)
wcUVAEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcUVAEnabled.setStatus("current")


class _WcOverLoadEnabled_Type(Integer32):
    """Custom type wcOverLoadEnabled based on Integer32"""
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


_WcOverLoadEnabled_Type.__name__ = "Integer32"
_WcOverLoadEnabled_Object = MibTableColumn
wcOverLoadEnabled = _WcOverLoadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 5),
    _WcOverLoadEnabled_Type()
)
wcOverLoadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcOverLoadEnabled.setStatus("current")


class _WcOverTemperatureEnabled_Type(Integer32):
    """Custom type wcOverTemperatureEnabled based on Integer32"""
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


_WcOverTemperatureEnabled_Type.__name__ = "Integer32"
_WcOverTemperatureEnabled_Object = MibTableColumn
wcOverTemperatureEnabled = _WcOverTemperatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 6),
    _WcOverTemperatureEnabled_Type()
)
wcOverTemperatureEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcOverTemperatureEnabled.setStatus("current")


class _WcShortCircuitEnabled_Type(Integer32):
    """Custom type wcShortCircuitEnabled based on Integer32"""
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


_WcShortCircuitEnabled_Type.__name__ = "Integer32"
_WcShortCircuitEnabled_Object = MibTableColumn
wcShortCircuitEnabled = _WcShortCircuitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 5, 1, 1, 7),
    _WcShortCircuitEnabled_Type()
)
wcShortCircuitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wcShortCircuitEnabled.setStatus("current")
_Warning_ObjectIdentity = ObjectIdentity
warning = _Warning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6)
)


class _WarningFanFault_Type(Integer32):
    """Custom type warningFanFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningFanFault_Type.__name__ = "Integer32"
_WarningFanFault_Object = MibScalar
warningFanFault = _WarningFanFault_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 1),
    _WarningFanFault_Type()
)
warningFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningFanFault.setStatus("current")


class _WarningOverVoltageAlarm_Type(Integer32):
    """Custom type warningOverVoltageAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningOverVoltageAlarm_Type.__name__ = "Integer32"
_WarningOverVoltageAlarm_Object = MibScalar
warningOverVoltageAlarm = _WarningOverVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 2),
    _WarningOverVoltageAlarm_Type()
)
warningOverVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningOverVoltageAlarm.setStatus("current")


class _WarningUnderVoltageAlarm_Type(Integer32):
    """Custom type warningUnderVoltageAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningUnderVoltageAlarm_Type.__name__ = "Integer32"
_WarningUnderVoltageAlarm_Object = MibScalar
warningUnderVoltageAlarm = _WarningUnderVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 3),
    _WarningUnderVoltageAlarm_Type()
)
warningUnderVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningUnderVoltageAlarm.setStatus("current")


class _WarningOverload_Type(Integer32):
    """Custom type warningOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningOverload_Type.__name__ = "Integer32"
_WarningOverload_Object = MibScalar
warningOverload = _WarningOverload_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 4),
    _WarningOverload_Type()
)
warningOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningOverload.setStatus("current")


class _WarningOverTemperature_Type(Integer32):
    """Custom type warningOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningOverTemperature_Type.__name__ = "Integer32"
_WarningOverTemperature_Object = MibScalar
warningOverTemperature = _WarningOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 5),
    _WarningOverTemperature_Type()
)
warningOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningOverTemperature.setStatus("current")


class _WarningShortCircuit_Type(Integer32):
    """Custom type warningShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningShortCircuit_Type.__name__ = "Integer32"
_WarningShortCircuit_Object = MibScalar
warningShortCircuit = _WarningShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 6),
    _WarningShortCircuit_Type()
)
warningShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningShortCircuit.setStatus("current")


class _WarningOverVoltageProtection_Type(Integer32):
    """Custom type warningOverVoltageProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningOverVoltageProtection_Type.__name__ = "Integer32"
_WarningOverVoltageProtection_Object = MibScalar
warningOverVoltageProtection = _WarningOverVoltageProtection_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 7),
    _WarningOverVoltageProtection_Type()
)
warningOverVoltageProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningOverVoltageProtection.setStatus("current")


class _WarningUnderVoltageProtection_Type(Integer32):
    """Custom type warningUnderVoltageProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1))
    )


_WarningUnderVoltageProtection_Type.__name__ = "Integer32"
_WarningUnderVoltageProtection_Object = MibScalar
warningUnderVoltageProtection = _WarningUnderVoltageProtection_Object(
    (1, 3, 6, 1, 4, 1, 49075, 1, 3, 6, 8),
    _WarningUnderVoltageProtection_Type()
)
warningUnderVoltageProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warningUnderVoltageProtection.setStatus("current")

# Managed Objects groups


# Notification objects

snmpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 49075, 1, 0, 1)
)
snmpTrap.setObjects(
      *(("SAMLEXAMERICA-MIB", "warningFanFault"),
        ("SAMLEXAMERICA-MIB", "warningOverVoltageAlarm"),
        ("SAMLEXAMERICA-MIB", "warningUnderVoltageAlarm"),
        ("SAMLEXAMERICA-MIB", "warningOverload"),
        ("SAMLEXAMERICA-MIB", "warningOverTemperature"),
        ("SAMLEXAMERICA-MIB", "warningShortCircuit"),
        ("SAMLEXAMERICA-MIB", "warningOverVoltageProtection"),
        ("SAMLEXAMERICA-MIB", "warningUnderVoltageProtection"))
)
if mibBuilder.loadTexts:
    snmpTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMLEXAMERICA-MIB",
    **{"samlexamerica": samlexamerica,
       "samlexamericaInfo": samlexamericaInfo,
       "trapNotifications": trapNotifications,
       "snmpTrap": snmpTrap,
       "product": product,
       "model": model,
       "version": version,
       "date": date,
       "setup": setup,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "telecom": telecom,
       "output": output,
       "cfgVout": cfgVout,
       "vout": vout,
       "iout": iout,
       "power": power,
       "cfgFrequency": cfgFrequency,
       "frequency": frequency,
       "gridvout": gridvout,
       "gridiout": gridiout,
       "gridpower": gridpower,
       "gridfrequency": gridfrequency,
       "input": input,
       "vin": vin,
       "ovp": ovp,
       "ovpRecovery": ovpRecovery,
       "uvp": uvp,
       "uvpRecovery": uvpRecovery,
       "ovAlarm": ovAlarm,
       "uvAlarm": uvAlarm,
       "status": status,
       "fan": fan,
       "inverterMode": inverterMode,
       "transferType": transferType,
       "byPassRelay": byPassRelay,
       "gridAC": gridAC,
       "olProtection": olProtection,
       "syncFreq": syncFreq,
       "tempDD": tempDD,
       "tempDA": tempDA,
       "ui": ui,
       "lcdContrast": lcdContrast,
       "lcdAutoOff": lcdAutoOff,
       "rs232Speed": rs232Speed,
       "usbVCOMSpeed": usbVCOMSpeed,
       "warningconfig": warningconfig,
       "wcTable": wcTable,
       "wcEntry": wcEntry,
       "wcIndex": wcIndex,
       "wcFanFaultEnabled": wcFanFaultEnabled,
       "wcOVAEnabled": wcOVAEnabled,
       "wcUVAEnabled": wcUVAEnabled,
       "wcOverLoadEnabled": wcOverLoadEnabled,
       "wcOverTemperatureEnabled": wcOverTemperatureEnabled,
       "wcShortCircuitEnabled": wcShortCircuitEnabled,
       "warning": warning,
       "warningFanFault": warningFanFault,
       "warningOverVoltageAlarm": warningOverVoltageAlarm,
       "warningUnderVoltageAlarm": warningUnderVoltageAlarm,
       "warningOverload": warningOverload,
       "warningOverTemperature": warningOverTemperature,
       "warningShortCircuit": warningShortCircuit,
       "warningOverVoltageProtection": warningOverVoltageProtection,
       "warningUnderVoltageProtection": warningUnderVoltageProtection}
)
