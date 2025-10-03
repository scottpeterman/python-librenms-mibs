# SNMP MIB module (TELTONIKA-RUTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teltonika\TELTONIKA-RUTM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:07 2025
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

teltonika = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48690)
)
if mibBuilder.loadTexts:
    teltonika.setRevisions(
        ("2025-06-12 23:18",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeltonikaSnmpGroups_ObjectIdentity = ObjectIdentity
teltonikaSnmpGroups = _TeltonikaSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 0)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 1)
)


class _Serial_Type(DisplayString):
    """Custom type serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Serial_Type.__name__ = "DisplayString"
_Serial_Object = MibScalar
serial = _Serial_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 1),
    _Serial_Type()
)
serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial.setStatus("current")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _ProductCode_Type(DisplayString):
    """Custom type productCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductCode_Type.__name__ = "DisplayString"
_ProductCode_Object = MibScalar
productCode = _ProductCode_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 3),
    _ProductCode_Type()
)
productCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productCode.setStatus("current")


class _BatchNumber_Type(DisplayString):
    """Custom type batchNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BatchNumber_Type.__name__ = "DisplayString"
_BatchNumber_Object = MibScalar
batchNumber = _BatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 4),
    _BatchNumber_Type()
)
batchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchNumber.setStatus("current")


class _HardwareRevision_Type(DisplayString):
    """Custom type hardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HardwareRevision_Type.__name__ = "DisplayString"
_HardwareRevision_Object = MibScalar
hardwareRevision = _HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 5),
    _HardwareRevision_Type()
)
hardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRevision.setStatus("current")


class _FwVersion_Type(DisplayString):
    """Custom type fwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwVersion_Type.__name__ = "DisplayString"
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 6),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")


class _DeviceUptime_Type(DisplayString):
    """Custom type deviceUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceUptime_Type.__name__ = "DisplayString"
_DeviceUptime_Object = MibScalar
deviceUptime = _DeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 7),
    _DeviceUptime_Type()
)
deviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUptime.setStatus("current")


class _CpuUsage_Type(DisplayString):
    """Custom type cpuUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpuUsage_Type.__name__ = "DisplayString"
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 8),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_Mobile_ObjectIdentity = ObjectIdentity
mobile = _Mobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 2)
)
_ModemNum_Type = Integer32
_ModemNum_Object = MibScalar
modemNum = _ModemNum_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 1),
    _ModemNum_Type()
)
modemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemNum.setStatus("current")
_ModemTable_Object = MibTable
modemTable = _ModemTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2)
)
if mibBuilder.loadTexts:
    modemTable.setStatus("current")
_ModemEntry_Object = MibTableRow
modemEntry = _ModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1)
)
modemEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "mIndex"),
)
if mibBuilder.loadTexts:
    modemEntry.setStatus("current")


class _MIndex_Type(Integer32):
    """Custom type mIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MIndex_Type.__name__ = "Integer32"
_MIndex_Object = MibTableColumn
mIndex = _MIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 1),
    _MIndex_Type()
)
mIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIndex.setStatus("current")


class _MDescr_Type(DisplayString):
    """Custom type mDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MDescr_Type.__name__ = "DisplayString"
_MDescr_Object = MibTableColumn
mDescr = _MDescr_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 2),
    _MDescr_Type()
)
mDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mDescr.setStatus("current")


class _MImei_Type(DisplayString):
    """Custom type mImei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MImei_Type.__name__ = "DisplayString"
_MImei_Object = MibTableColumn
mImei = _MImei_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 3),
    _MImei_Type()
)
mImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mImei.setStatus("current")


class _MModel_Type(DisplayString):
    """Custom type mModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MModel_Type.__name__ = "DisplayString"
_MModel_Object = MibTableColumn
mModel = _MModel_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 4),
    _MModel_Type()
)
mModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mModel.setStatus("current")


class _MManufacturer_Type(DisplayString):
    """Custom type mManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MManufacturer_Type.__name__ = "DisplayString"
_MManufacturer_Object = MibTableColumn
mManufacturer = _MManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 5),
    _MManufacturer_Type()
)
mManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mManufacturer.setStatus("current")


class _MRevision_Type(DisplayString):
    """Custom type mRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MRevision_Type.__name__ = "DisplayString"
_MRevision_Object = MibTableColumn
mRevision = _MRevision_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 6),
    _MRevision_Type()
)
mRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRevision.setStatus("current")


class _MSerial_Type(DisplayString):
    """Custom type mSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MSerial_Type.__name__ = "DisplayString"
_MSerial_Object = MibTableColumn
mSerial = _MSerial_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 7),
    _MSerial_Type()
)
mSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSerial.setStatus("current")


class _MIMSI_Type(DisplayString):
    """Custom type mIMSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MIMSI_Type.__name__ = "DisplayString"
_MIMSI_Object = MibTableColumn
mIMSI = _MIMSI_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 8),
    _MIMSI_Type()
)
mIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIMSI.setStatus("current")


class _MSimState_Type(DisplayString):
    """Custom type mSimState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MSimState_Type.__name__ = "DisplayString"
_MSimState_Object = MibTableColumn
mSimState = _MSimState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 9),
    _MSimState_Type()
)
mSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSimState.setStatus("current")


class _MPinState_Type(DisplayString):
    """Custom type mPinState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MPinState_Type.__name__ = "DisplayString"
_MPinState_Object = MibTableColumn
mPinState = _MPinState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 10),
    _MPinState_Type()
)
mPinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPinState.setStatus("current")


class _MNetState_Type(DisplayString):
    """Custom type mNetState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MNetState_Type.__name__ = "DisplayString"
_MNetState_Object = MibTableColumn
mNetState = _MNetState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 11),
    _MNetState_Type()
)
mNetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNetState.setStatus("current")


class _MSignal_Type(DisplayString):
    """Custom type mSignal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MSignal_Type.__name__ = "DisplayString"
_MSignal_Object = MibTableColumn
mSignal = _MSignal_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 12),
    _MSignal_Type()
)
mSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSignal.setStatus("current")


class _MOperator_Type(DisplayString):
    """Custom type mOperator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MOperator_Type.__name__ = "DisplayString"
_MOperator_Object = MibTableColumn
mOperator = _MOperator_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 13),
    _MOperator_Type()
)
mOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mOperator.setStatus("current")


class _MOperatorNumber_Type(DisplayString):
    """Custom type mOperatorNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MOperatorNumber_Type.__name__ = "DisplayString"
_MOperatorNumber_Object = MibTableColumn
mOperatorNumber = _MOperatorNumber_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 14),
    _MOperatorNumber_Type()
)
mOperatorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mOperatorNumber.setStatus("current")


class _MConnectionState_Type(DisplayString):
    """Custom type mConnectionState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MConnectionState_Type.__name__ = "DisplayString"
_MConnectionState_Object = MibTableColumn
mConnectionState = _MConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 15),
    _MConnectionState_Type()
)
mConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mConnectionState.setStatus("current")


class _MNetworkType_Type(DisplayString):
    """Custom type mNetworkType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MNetworkType_Type.__name__ = "DisplayString"
_MNetworkType_Object = MibTableColumn
mNetworkType = _MNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 16),
    _MNetworkType_Type()
)
mNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNetworkType.setStatus("current")
_MTemperature_Type = Integer32
_MTemperature_Object = MibTableColumn
mTemperature = _MTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 17),
    _MTemperature_Type()
)
mTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTemperature.setStatus("current")


class _MCellID_Type(DisplayString):
    """Custom type mCellID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MCellID_Type.__name__ = "DisplayString"
_MCellID_Object = MibTableColumn
mCellID = _MCellID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 18),
    _MCellID_Type()
)
mCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCellID.setStatus("current")


class _MSINR_Type(DisplayString):
    """Custom type mSINR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MSINR_Type.__name__ = "DisplayString"
_MSINR_Object = MibTableColumn
mSINR = _MSINR_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 19),
    _MSINR_Type()
)
mSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSINR.setStatus("current")


class _MRSRP_Type(DisplayString):
    """Custom type mRSRP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MRSRP_Type.__name__ = "DisplayString"
_MRSRP_Object = MibTableColumn
mRSRP = _MRSRP_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 20),
    _MRSRP_Type()
)
mRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRSRP.setStatus("current")


class _MRSRQ_Type(DisplayString):
    """Custom type mRSRQ based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MRSRQ_Type.__name__ = "DisplayString"
_MRSRQ_Object = MibTableColumn
mRSRQ = _MRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 21),
    _MRSRQ_Type()
)
mRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRSRQ.setStatus("current")
_MSent_Type = Counter64
_MSent_Object = MibTableColumn
mSent = _MSent_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 22),
    _MSent_Type()
)
mSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSent.setStatus("current")
_MReceived_Type = Counter64
_MReceived_Object = MibTableColumn
mReceived = _MReceived_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 23),
    _MReceived_Type()
)
mReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mReceived.setStatus("current")


class _MIP_Type(DisplayString):
    """Custom type mIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MIP_Type.__name__ = "DisplayString"
_MIP_Object = MibTableColumn
mIP = _MIP_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 24),
    _MIP_Type()
)
mIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIP.setStatus("current")
_MSentToday_Type = Counter64
_MSentToday_Object = MibTableColumn
mSentToday = _MSentToday_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 25),
    _MSentToday_Type()
)
mSentToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSentToday.setStatus("current")
_MReceivedToday_Type = Counter64
_MReceivedToday_Object = MibTableColumn
mReceivedToday = _MReceivedToday_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 26),
    _MReceivedToday_Type()
)
mReceivedToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mReceivedToday.setStatus("current")


class _MICCID_Type(DisplayString):
    """Custom type mICCID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MICCID_Type.__name__ = "DisplayString"
_MICCID_Object = MibTableColumn
mICCID = _MICCID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 27),
    _MICCID_Type()
)
mICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mICCID.setStatus("current")
_MSentCurrentWeek_Type = Counter64
_MSentCurrentWeek_Object = MibTableColumn
mSentCurrentWeek = _MSentCurrentWeek_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 28),
    _MSentCurrentWeek_Type()
)
mSentCurrentWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSentCurrentWeek.setStatus("current")
_MReceivedCurrentWeek_Type = Counter64
_MReceivedCurrentWeek_Object = MibTableColumn
mReceivedCurrentWeek = _MReceivedCurrentWeek_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 29),
    _MReceivedCurrentWeek_Type()
)
mReceivedCurrentWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mReceivedCurrentWeek.setStatus("current")
_MSentCurrentMonth_Type = Counter64
_MSentCurrentMonth_Object = MibTableColumn
mSentCurrentMonth = _MSentCurrentMonth_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 30),
    _MSentCurrentMonth_Type()
)
mSentCurrentMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSentCurrentMonth.setStatus("current")
_MReceivedCurrentMonth_Type = Counter64
_MReceivedCurrentMonth_Object = MibTableColumn
mReceivedCurrentMonth = _MReceivedCurrentMonth_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 31),
    _MReceivedCurrentMonth_Type()
)
mReceivedCurrentMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mReceivedCurrentMonth.setStatus("current")
_ConnectionUptime_Type = Unsigned32
_ConnectionUptime_Object = MibScalar
connectionUptime = _ConnectionUptime_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 3),
    _ConnectionUptime_Type()
)
connectionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionUptime.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 3)
)


class _Latitude_Type(DisplayString):
    """Custom type latitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Latitude_Type.__name__ = "DisplayString"
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 48690, 3, 1),
    _Latitude_Type()
)
latitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latitude.setStatus("current")


class _Longtitude_Type(DisplayString):
    """Custom type longtitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Longtitude_Type.__name__ = "DisplayString"
_Longtitude_Object = MibScalar
longtitude = _Longtitude_Object(
    (1, 3, 6, 1, 4, 1, 48690, 3, 2),
    _Longtitude_Type()
)
longtitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    longtitude.setStatus("current")


class _Accuracy_Type(DisplayString):
    """Custom type accuracy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Accuracy_Type.__name__ = "DisplayString"
_Accuracy_Object = MibScalar
accuracy = _Accuracy_Object(
    (1, 3, 6, 1, 4, 1, 48690, 3, 3),
    _Accuracy_Type()
)
accuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accuracy.setStatus("current")


class _Datetime_Type(DisplayString):
    """Custom type datetime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Datetime_Type.__name__ = "DisplayString"
_Datetime_Object = MibScalar
datetime = _Datetime_Object(
    (1, 3, 6, 1, 4, 1, 48690, 3, 4),
    _Datetime_Type()
)
datetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datetime.setStatus("current")
_NumSatellites_Type = Integer32
_NumSatellites_Object = MibScalar
numSatellites = _NumSatellites_Object(
    (1, 3, 6, 1, 4, 1, 48690, 3, 5),
    _NumSatellites_Type()
)
numSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSatellites.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4)
)
_MobileNotifications_ObjectIdentity = ObjectIdentity
mobileNotifications = _MobileNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4, 1)
)
_IoNotifications_ObjectIdentity = ObjectIdentity
ioNotifications = _IoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2)
)
_HotspotNotifications_ObjectIdentity = ObjectIdentity
hotspotNotifications = _HotspotNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4, 3)
)
_EventNotifications_ObjectIdentity = ObjectIdentity
eventNotifications = _EventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4, 4)
)
_Hotspot_ObjectIdentity = ObjectIdentity
hotspot = _Hotspot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 5)
)


class _HsState_Type(Integer32):
    """Custom type hsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HsState_Type.__name__ = "Integer32"
_HsState_Object = MibScalar
hsState = _HsState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 1),
    _HsState_Type()
)
hsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsState.setStatus("current")
_HsIP_Type = IpAddress
_HsIP_Object = MibScalar
hsIP = _HsIP_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 2),
    _HsIP_Type()
)
hsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsIP.setStatus("current")


class _HsNet_Type(DisplayString):
    """Custom type hsNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HsNet_Type.__name__ = "DisplayString"
_HsNet_Object = MibScalar
hsNet = _HsNet_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 3),
    _HsNet_Type()
)
hsNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsNet.setStatus("current")


class _HsAuth_Type(DisplayString):
    """Custom type hsAuth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HsAuth_Type.__name__ = "DisplayString"
_HsAuth_Object = MibScalar
hsAuth = _HsAuth_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 4),
    _HsAuth_Type()
)
hsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsAuth.setStatus("current")
_HsSessionCount_Type = Counter64
_HsSessionCount_Object = MibScalar
hsSessionCount = _HsSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 5),
    _HsSessionCount_Type()
)
hsSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsSessionCount.setStatus("current")
_HsSessionTable_Object = MibTable
hsSessionTable = _HsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6)
)
if mibBuilder.loadTexts:
    hsSessionTable.setStatus("current")
_HsSessionEntry_Object = MibTableRow
hsSessionEntry = _HsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1)
)
hsSessionEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "hssIndex"),
)
if mibBuilder.loadTexts:
    hsSessionEntry.setStatus("current")


class _HssIndex_Type(Integer32):
    """Custom type hssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HssIndex_Type.__name__ = "Integer32"
_HssIndex_Object = MibTableColumn
hssIndex = _HssIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 1),
    _HssIndex_Type()
)
hssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssIndex.setStatus("current")
_HssMAC_Type = PhysAddress
_HssMAC_Object = MibTableColumn
hssMAC = _HssMAC_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 2),
    _HssMAC_Type()
)
hssMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssMAC.setStatus("current")
_HssIP_Type = IpAddress
_HssIP_Object = MibTableColumn
hssIP = _HssIP_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 3),
    _HssIP_Type()
)
hssIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssIP.setStatus("current")
_HssID_Type = DisplayString
_HssID_Object = MibTableColumn
hssID = _HssID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 4),
    _HssID_Type()
)
hssID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssID.setStatus("current")


class _HssUsername_Type(DisplayString):
    """Custom type hssUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HssUsername_Type.__name__ = "DisplayString"
_HssUsername_Object = MibTableColumn
hssUsername = _HssUsername_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 5),
    _HssUsername_Type()
)
hssUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssUsername.setStatus("current")


class _HssState_Type(Integer32):
    """Custom type hssState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAuthorized", 0),
          ("authorized", 1))
    )


_HssState_Type.__name__ = "Integer32"
_HssState_Object = MibTableColumn
hssState = _HssState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 6),
    _HssState_Type()
)
hssState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssState.setStatus("current")
_HssDwLimit_Type = Counter64
_HssDwLimit_Object = MibTableColumn
hssDwLimit = _HssDwLimit_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 7),
    _HssDwLimit_Type()
)
hssDwLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssDwLimit.setStatus("current")
_HssUpLimit_Type = Counter64
_HssUpLimit_Object = MibTableColumn
hssUpLimit = _HssUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 8),
    _HssUpLimit_Type()
)
hssUpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssUpLimit.setStatus("current")
_HssTimeLimit_Type = Counter64
_HssTimeLimit_Object = MibTableColumn
hssTimeLimit = _HssTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 9),
    _HssTimeLimit_Type()
)
hssTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssTimeLimit.setStatus("current")
_HssIdleTimeout_Type = Integer32
_HssIdleTimeout_Object = MibTableColumn
hssIdleTimeout = _HssIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 10),
    _HssIdleTimeout_Type()
)
hssIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssIdleTimeout.setStatus("current")
_HssDwBandwidth_Type = Counter64
_HssDwBandwidth_Object = MibTableColumn
hssDwBandwidth = _HssDwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 11),
    _HssDwBandwidth_Type()
)
hssDwBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssDwBandwidth.setStatus("current")
_HssUpBandwidth_Type = Counter64
_HssUpBandwidth_Object = MibTableColumn
hssUpBandwidth = _HssUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 12),
    _HssUpBandwidth_Type()
)
hssUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssUpBandwidth.setStatus("current")
_HssURL_Type = DisplayString
_HssURL_Object = MibTableColumn
hssURL = _HssURL_Object(
    (1, 3, 6, 1, 4, 1, 48690, 5, 6, 1, 13),
    _HssURL_Type()
)
hssURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssURL.setStatus("current")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 6)
)
_IoCount_Type = Integer32
_IoCount_Object = MibScalar
ioCount = _IoCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 1),
    _IoCount_Type()
)
ioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioCount.setStatus("current")
_IoTable_Object = MibTable
ioTable = _IoTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2)
)
if mibBuilder.loadTexts:
    ioTable.setStatus("current")
_IoEntry_Object = MibTableRow
ioEntry = _IoEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1)
)
ioEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "ioIndex"),
)
if mibBuilder.loadTexts:
    ioEntry.setStatus("current")


class _IoIndex_Type(Integer32):
    """Custom type ioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IoIndex_Type.__name__ = "Integer32"
_IoIndex_Object = MibTableColumn
ioIndex = _IoIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 1),
    _IoIndex_Type()
)
ioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioIndex.setStatus("current")
_IoSystemName_Type = DisplayString
_IoSystemName_Object = MibTableColumn
ioSystemName = _IoSystemName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 2),
    _IoSystemName_Type()
)
ioSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSystemName.setStatus("current")
_IoName_Type = DisplayString
_IoName_Object = MibTableColumn
ioName = _IoName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 3),
    _IoName_Type()
)
ioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioName.setStatus("current")
_IoType_Type = DisplayString
_IoType_Object = MibTableColumn
ioType = _IoType_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 4),
    _IoType_Type()
)
ioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioType.setStatus("current")
_IoBidirectional_Type = Integer32
_IoBidirectional_Object = MibTableColumn
ioBidirectional = _IoBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 5),
    _IoBidirectional_Type()
)
ioBidirectional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioBidirectional.setStatus("current")
_IoState_Type = DisplayString
_IoState_Object = MibTableColumn
ioState = _IoState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 6),
    _IoState_Type()
)
ioState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioState.setStatus("current")
_IoInput_Type = Integer32
_IoInput_Object = MibTableColumn
ioInput = _IoInput_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 7),
    _IoInput_Type()
)
ioInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioInput.setStatus("current")
_IoInverted_Type = Integer32
_IoInverted_Object = MibTableColumn
ioInverted = _IoInverted_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 8),
    _IoInverted_Type()
)
ioInverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioInverted.setStatus("current")
_IoCurrent_Type = DisplayString
_IoCurrent_Object = MibTableColumn
ioCurrent = _IoCurrent_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 9),
    _IoCurrent_Type()
)
ioCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioCurrent.setStatus("current")
_IoPercentage_Type = DisplayString
_IoPercentage_Object = MibTableColumn
ioPercentage = _IoPercentage_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 10),
    _IoPercentage_Type()
)
ioPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioPercentage.setStatus("current")


class _IoStateNumeric_Type(Integer32):
    """Custom type ioStateNumeric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("low", 0),
          ("high", 1))
    )


_IoStateNumeric_Type.__name__ = "Integer32"
_IoStateNumeric_Object = MibTableColumn
ioStateNumeric = _IoStateNumeric_Object(
    (1, 3, 6, 1, 4, 1, 48690, 6, 2, 1, 11),
    _IoStateNumeric_Type()
)
ioStateNumeric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioStateNumeric.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 7)
)
_RadioCount_Type = Integer32
_RadioCount_Object = MibScalar
radioCount = _RadioCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 1),
    _RadioCount_Type()
)
radioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCount.setStatus("current")
_RadioTable_Object = MibTable
radioTable = _RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2)
)
if mibBuilder.loadTexts:
    radioTable.setStatus("current")
_RadioEntry_Object = MibTableRow
radioEntry = _RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1)
)
radioEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioEntry.setStatus("current")


class _RadioIndex_Type(Integer32):
    """Custom type radioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadioIndex_Type.__name__ = "Integer32"
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIndex.setStatus("current")
_RadioName_Type = DisplayString
_RadioName_Object = MibTableColumn
radioName = _RadioName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1, 2),
    _RadioName_Type()
)
radioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioName.setStatus("current")
_RadioUpState_Type = Integer32
_RadioUpState_Object = MibTableColumn
radioUpState = _RadioUpState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1, 3),
    _RadioUpState_Type()
)
radioUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioUpState.setStatus("current")
_RadioDisabledState_Type = Integer32
_RadioDisabledState_Object = MibTableColumn
radioDisabledState = _RadioDisabledState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1, 4),
    _RadioDisabledState_Type()
)
radioDisabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDisabledState.setStatus("current")
_RadioChannel_Type = DisplayString
_RadioChannel_Object = MibTableColumn
radioChannel = _RadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 2, 1, 5),
    _RadioChannel_Type()
)
radioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannel.setStatus("current")
_WIfaceCount_Type = Integer32
_WIfaceCount_Object = MibScalar
wIfaceCount = _WIfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 3),
    _WIfaceCount_Type()
)
wIfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceCount.setStatus("current")
_WIfaceTable_Object = MibTable
wIfaceTable = _WIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4)
)
if mibBuilder.loadTexts:
    wIfaceTable.setStatus("current")
_WIfaceEntry_Object = MibTableRow
wIfaceEntry = _WIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1)
)
wIfaceEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "wIfaceIndex"),
)
if mibBuilder.loadTexts:
    wIfaceEntry.setStatus("current")


class _WIfaceIndex_Type(Integer32):
    """Custom type wIfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WIfaceIndex_Type.__name__ = "Integer32"
_WIfaceIndex_Object = MibTableColumn
wIfaceIndex = _WIfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1, 1),
    _WIfaceIndex_Type()
)
wIfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceIndex.setStatus("current")
_WIfaceSSID_Type = DisplayString
_WIfaceSSID_Object = MibTableColumn
wIfaceSSID = _WIfaceSSID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1, 2),
    _WIfaceSSID_Type()
)
wIfaceSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceSSID.setStatus("current")
_WIfaceHidden_Type = Integer32
_WIfaceHidden_Object = MibTableColumn
wIfaceHidden = _WIfaceHidden_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1, 3),
    _WIfaceHidden_Type()
)
wIfaceHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceHidden.setStatus("current")
_WIfaceEncryption_Type = DisplayString
_WIfaceEncryption_Object = MibTableColumn
wIfaceEncryption = _WIfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1, 4),
    _WIfaceEncryption_Type()
)
wIfaceEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceEncryption.setStatus("current")
_WIfaceMode_Type = DisplayString
_WIfaceMode_Object = MibTableColumn
wIfaceMode = _WIfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 48690, 7, 4, 1, 5),
    _WIfaceMode_Type()
)
wIfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wIfaceMode.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 8)
)
_PVlanCount_Type = Integer32
_PVlanCount_Object = MibScalar
pVlanCount = _PVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 1),
    _PVlanCount_Type()
)
pVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanCount.setStatus("current")
_PVlanTable_Object = MibTable
pVlanTable = _PVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2)
)
if mibBuilder.loadTexts:
    pVlanTable.setStatus("current")
_PVlanEntry_Object = MibTableRow
pVlanEntry = _PVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2, 1)
)
pVlanEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "pVlanIndex"),
)
if mibBuilder.loadTexts:
    pVlanEntry.setStatus("current")


class _PVlanIndex_Type(Integer32):
    """Custom type pVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PVlanIndex_Type.__name__ = "Integer32"
_PVlanIndex_Object = MibTableColumn
pVlanIndex = _PVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2, 1, 1),
    _PVlanIndex_Type()
)
pVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanIndex.setStatus("current")
_PVlanNum_Type = Integer32
_PVlanNum_Object = MibTableColumn
pVlanNum = _PVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2, 1, 2),
    _PVlanNum_Type()
)
pVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanNum.setStatus("current")
_PVlanPorts_Type = DisplayString
_PVlanPorts_Object = MibTableColumn
pVlanPorts = _PVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2, 1, 3),
    _PVlanPorts_Type()
)
pVlanPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanPorts.setStatus("current")
_PVlanVID_Type = DisplayString
_PVlanVID_Object = MibTableColumn
pVlanVID = _PVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 2, 1, 4),
    _PVlanVID_Type()
)
pVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanVID.setStatus("current")
_IVlanCount_Type = Integer32
_IVlanCount_Object = MibScalar
iVlanCount = _IVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 3),
    _IVlanCount_Type()
)
iVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanCount.setStatus("current")
_IVlanTable_Object = MibTable
iVlanTable = _IVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4)
)
if mibBuilder.loadTexts:
    iVlanTable.setStatus("current")
_IVlanEntry_Object = MibTableRow
iVlanEntry = _IVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1)
)
iVlanEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "iVlanIndex"),
)
if mibBuilder.loadTexts:
    iVlanEntry.setStatus("current")


class _IVlanIndex_Type(Integer32):
    """Custom type iVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IVlanIndex_Type.__name__ = "Integer32"
_IVlanIndex_Object = MibTableColumn
iVlanIndex = _IVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1, 1),
    _IVlanIndex_Type()
)
iVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanIndex.setStatus("current")
_IVlanName_Type = DisplayString
_IVlanName_Object = MibTableColumn
iVlanName = _IVlanName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1, 2),
    _IVlanName_Type()
)
iVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanName.setStatus("current")
_IVlanType_Type = DisplayString
_IVlanType_Object = MibTableColumn
iVlanType = _IVlanType_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1, 3),
    _IVlanType_Type()
)
iVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanType.setStatus("current")
_IVlanIfName_Type = DisplayString
_IVlanIfName_Object = MibTableColumn
iVlanIfName = _IVlanIfName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1, 4),
    _IVlanIfName_Type()
)
iVlanIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanIfName.setStatus("current")
_IVlanVID_Type = Integer32
_IVlanVID_Object = MibTableColumn
iVlanVID = _IVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 4, 1, 5),
    _IVlanVID_Type()
)
iVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVlanVID.setStatus("current")
_Sqm_ObjectIdentity = ObjectIdentity
sqm = _Sqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 9)
)
_QueueCount_Type = Integer32
_QueueCount_Object = MibScalar
queueCount = _QueueCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 1),
    _QueueCount_Type()
)
queueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueCount.setStatus("current")
_QueueTable_Object = MibTable
queueTable = _QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2)
)
if mibBuilder.loadTexts:
    queueTable.setStatus("current")
_QueueEntry_Object = MibTableRow
queueEntry = _QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1)
)
queueEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "queueIndex"),
)
if mibBuilder.loadTexts:
    queueEntry.setStatus("current")


class _QueueIndex_Type(Integer32):
    """Custom type queueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QueueIndex_Type.__name__ = "Integer32"
_QueueIndex_Object = MibTableColumn
queueIndex = _QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 1),
    _QueueIndex_Type()
)
queueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueIndex.setStatus("current")
_QueueName_Type = DisplayString
_QueueName_Object = MibTableColumn
queueName = _QueueName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 2),
    _QueueName_Type()
)
queueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueName.setStatus("current")
_QueueEnabled_Type = Integer32
_QueueEnabled_Object = MibTableColumn
queueEnabled = _QueueEnabled_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 3),
    _QueueEnabled_Type()
)
queueEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueEnabled.setStatus("current")
_QueueIface_Type = DisplayString
_QueueIface_Object = MibTableColumn
queueIface = _QueueIface_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 4),
    _QueueIface_Type()
)
queueIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueIface.setStatus("current")
_QueueDownLimit_Type = Integer32
_QueueDownLimit_Object = MibTableColumn
queueDownLimit = _QueueDownLimit_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 5),
    _QueueDownLimit_Type()
)
queueDownLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueDownLimit.setStatus("current")
_QueueUpLimit_Type = Integer32
_QueueUpLimit_Object = MibTableColumn
queueUpLimit = _QueueUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 6),
    _QueueUpLimit_Type()
)
queueUpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueUpLimit.setStatus("current")
_QueueQdisk_Type = DisplayString
_QueueQdisk_Object = MibTableColumn
queueQdisk = _QueueQdisk_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 7),
    _QueueQdisk_Type()
)
queueQdisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueQdisk.setStatus("current")
_QueueScript_Type = DisplayString
_QueueScript_Object = MibTableColumn
queueScript = _QueueScript_Object(
    (1, 3, 6, 1, 4, 1, 48690, 9, 2, 1, 8),
    _QueueScript_Type()
)
queueScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueScript.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 10)
)
_PortCount_Type = Integer32
_PortCount_Object = MibScalar
portCount = _PortCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 1),
    _PortCount_Type()
)
portCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCount.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1)
)
portEntry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "pIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PIndex_Type(Integer32):
    """Custom type pIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PIndex_Type.__name__ = "Integer32"
_PIndex_Object = MibTableColumn
pIndex = _PIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 1),
    _PIndex_Type()
)
pIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pIndex.setStatus("current")


class _PName_Type(DisplayString):
    """Custom type pName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PName_Type.__name__ = "DisplayString"
_PName_Object = MibTableColumn
pName = _PName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 2),
    _PName_Type()
)
pName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pName.setStatus("current")
_PNumber_Type = Integer32
_PNumber_Object = MibTableColumn
pNumber = _PNumber_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 3),
    _PNumber_Type()
)
pNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNumber.setStatus("current")
_PPosition_Type = Integer32
_PPosition_Object = MibTableColumn
pPosition = _PPosition_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 4),
    _PPosition_Type()
)
pPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPosition.setStatus("current")


class _PState_Type(DisplayString):
    """Custom type pState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PState_Type.__name__ = "DisplayString"
_PState_Object = MibTableColumn
pState = _PState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 5),
    _PState_Type()
)
pState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pState.setStatus("current")
_PSpeed_Type = Integer32
_PSpeed_Object = MibTableColumn
pSpeed = _PSpeed_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 6),
    _PSpeed_Type()
)
pSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSpeed.setStatus("current")


class _PDuplex_Type(DisplayString):
    """Custom type pDuplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PDuplex_Type.__name__ = "DisplayString"
_PDuplex_Object = MibTableColumn
pDuplex = _PDuplex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 10, 2, 1, 7),
    _PDuplex_Type()
)
pDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDuplex.setStatus("current")
_Mwan3_ObjectIdentity = ObjectIdentity
mwan3 = _Mwan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 12)
)
_Mwan3Count_Type = Integer32
_Mwan3Count_Object = MibScalar
mwan3Count = _Mwan3Count_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 1),
    _Mwan3Count_Type()
)
mwan3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Count.setStatus("current")
_Mwan3Table_Object = MibTable
mwan3Table = _Mwan3Table_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2)
)
if mibBuilder.loadTexts:
    mwan3Table.setStatus("current")
_Mwan3Entry_Object = MibTableRow
mwan3Entry = _Mwan3Entry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1)
)
mwan3Entry.setIndexNames(
    (0, "TELTONIKA-RUTM-MIB", "mwan3Index"),
)
if mibBuilder.loadTexts:
    mwan3Entry.setStatus("current")


class _Mwan3Index_Type(Integer32):
    """Custom type mwan3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mwan3Index_Type.__name__ = "Integer32"
_Mwan3Index_Object = MibTableColumn
mwan3Index = _Mwan3Index_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 1),
    _Mwan3Index_Type()
)
mwan3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Index.setStatus("current")
_Mwan3Name_Type = DisplayString
_Mwan3Name_Object = MibTableColumn
mwan3Name = _Mwan3Name_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 2),
    _Mwan3Name_Type()
)
mwan3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Name.setStatus("current")
_Mwan3Enabled_Type = Integer32
_Mwan3Enabled_Object = MibTableColumn
mwan3Enabled = _Mwan3Enabled_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 3),
    _Mwan3Enabled_Type()
)
mwan3Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Enabled.setStatus("current")
_Mwan3Uptime_Type = Integer32
_Mwan3Uptime_Object = MibTableColumn
mwan3Uptime = _Mwan3Uptime_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 4),
    _Mwan3Uptime_Type()
)
mwan3Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Uptime.setStatus("current")
_Mwan3Status_Type = DisplayString
_Mwan3Status_Object = MibTableColumn
mwan3Status = _Mwan3Status_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 5),
    _Mwan3Status_Type()
)
mwan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Status.setStatus("current")
_Mwan3Ip_Type = DisplayString
_Mwan3Ip_Object = MibTableColumn
mwan3Ip = _Mwan3Ip_Object(
    (1, 3, 6, 1, 4, 1, 48690, 12, 2, 1, 6),
    _Mwan3Ip_Type()
)
mwan3Ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwan3Ip.setStatus("current")

# Managed Objects groups

deviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 1)
)
deviceGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "serial"),
        ("TELTONIKA-RUTM-MIB", "deviceName"),
        ("TELTONIKA-RUTM-MIB", "productCode"),
        ("TELTONIKA-RUTM-MIB", "batchNumber"),
        ("TELTONIKA-RUTM-MIB", "hardwareRevision"),
        ("TELTONIKA-RUTM-MIB", "fwVersion"),
        ("TELTONIKA-RUTM-MIB", "deviceUptime"),
        ("TELTONIKA-RUTM-MIB", "cpuUsage"))
)
if mibBuilder.loadTexts:
    deviceGroup.setStatus("current")

modemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 2)
)
modemGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "modemNum"),
        ("TELTONIKA-RUTM-MIB", "mIndex"),
        ("TELTONIKA-RUTM-MIB", "mDescr"),
        ("TELTONIKA-RUTM-MIB", "mImei"),
        ("TELTONIKA-RUTM-MIB", "mModel"),
        ("TELTONIKA-RUTM-MIB", "mManufacturer"),
        ("TELTONIKA-RUTM-MIB", "mRevision"),
        ("TELTONIKA-RUTM-MIB", "mSerial"),
        ("TELTONIKA-RUTM-MIB", "mIMSI"),
        ("TELTONIKA-RUTM-MIB", "mSimState"),
        ("TELTONIKA-RUTM-MIB", "mPinState"),
        ("TELTONIKA-RUTM-MIB", "mNetState"),
        ("TELTONIKA-RUTM-MIB", "mSignal"),
        ("TELTONIKA-RUTM-MIB", "mOperator"),
        ("TELTONIKA-RUTM-MIB", "mOperatorNumber"),
        ("TELTONIKA-RUTM-MIB", "mConnectionState"),
        ("TELTONIKA-RUTM-MIB", "mNetworkType"),
        ("TELTONIKA-RUTM-MIB", "mTemperature"),
        ("TELTONIKA-RUTM-MIB", "mCellID"),
        ("TELTONIKA-RUTM-MIB", "mSINR"),
        ("TELTONIKA-RUTM-MIB", "mRSRP"),
        ("TELTONIKA-RUTM-MIB", "mRSRQ"),
        ("TELTONIKA-RUTM-MIB", "mSent"),
        ("TELTONIKA-RUTM-MIB", "mReceived"),
        ("TELTONIKA-RUTM-MIB", "mIP"),
        ("TELTONIKA-RUTM-MIB", "mSentToday"),
        ("TELTONIKA-RUTM-MIB", "mReceivedToday"),
        ("TELTONIKA-RUTM-MIB", "mICCID"),
        ("TELTONIKA-RUTM-MIB", "mSentCurrentWeek"),
        ("TELTONIKA-RUTM-MIB", "mReceivedCurrentWeek"),
        ("TELTONIKA-RUTM-MIB", "mSentCurrentMonth"),
        ("TELTONIKA-RUTM-MIB", "mReceivedCurrentMonth"),
        ("TELTONIKA-RUTM-MIB", "connectionUptime"))
)
if mibBuilder.loadTexts:
    modemGroup.setStatus("current")

hotspotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 5)
)
hotspotGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "hsState"),
        ("TELTONIKA-RUTM-MIB", "hsIP"),
        ("TELTONIKA-RUTM-MIB", "hsNet"),
        ("TELTONIKA-RUTM-MIB", "hsAuth"),
        ("TELTONIKA-RUTM-MIB", "hsSessionCount"),
        ("TELTONIKA-RUTM-MIB", "hssIndex"),
        ("TELTONIKA-RUTM-MIB", "hssMAC"),
        ("TELTONIKA-RUTM-MIB", "hssIP"),
        ("TELTONIKA-RUTM-MIB", "hssID"),
        ("TELTONIKA-RUTM-MIB", "hssUsername"),
        ("TELTONIKA-RUTM-MIB", "hssState"),
        ("TELTONIKA-RUTM-MIB", "hssDwLimit"),
        ("TELTONIKA-RUTM-MIB", "hssUpLimit"),
        ("TELTONIKA-RUTM-MIB", "hssTimeLimit"),
        ("TELTONIKA-RUTM-MIB", "hssIdleTimeout"),
        ("TELTONIKA-RUTM-MIB", "hssDwBandwidth"),
        ("TELTONIKA-RUTM-MIB", "hssUpBandwidth"),
        ("TELTONIKA-RUTM-MIB", "hssURL"))
)
if mibBuilder.loadTexts:
    hotspotGroup.setStatus("current")

ioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 6)
)
ioGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "ioCount"),
        ("TELTONIKA-RUTM-MIB", "ioIndex"),
        ("TELTONIKA-RUTM-MIB", "ioSystemName"),
        ("TELTONIKA-RUTM-MIB", "ioName"),
        ("TELTONIKA-RUTM-MIB", "ioType"),
        ("TELTONIKA-RUTM-MIB", "ioBidirectional"),
        ("TELTONIKA-RUTM-MIB", "ioState"),
        ("TELTONIKA-RUTM-MIB", "ioInput"),
        ("TELTONIKA-RUTM-MIB", "ioInverted"),
        ("TELTONIKA-RUTM-MIB", "ioCurrent"),
        ("TELTONIKA-RUTM-MIB", "ioPercentage"),
        ("TELTONIKA-RUTM-MIB", "ioStateNumeric"))
)
if mibBuilder.loadTexts:
    ioGroup.setStatus("current")

radioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 7)
)
radioGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "radioCount"),
        ("TELTONIKA-RUTM-MIB", "radioIndex"),
        ("TELTONIKA-RUTM-MIB", "radioName"),
        ("TELTONIKA-RUTM-MIB", "radioUpState"),
        ("TELTONIKA-RUTM-MIB", "radioDisabledState"),
        ("TELTONIKA-RUTM-MIB", "radioChannel"))
)
if mibBuilder.loadTexts:
    radioGroup.setStatus("current")

wIfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 8)
)
wIfaceGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "wIfaceCount"),
        ("TELTONIKA-RUTM-MIB", "wIfaceIndex"),
        ("TELTONIKA-RUTM-MIB", "wIfaceSSID"),
        ("TELTONIKA-RUTM-MIB", "wIfaceHidden"),
        ("TELTONIKA-RUTM-MIB", "wIfaceEncryption"),
        ("TELTONIKA-RUTM-MIB", "wIfaceMode"))
)
if mibBuilder.loadTexts:
    wIfaceGroup.setStatus("current")

iVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 9)
)
iVlanGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "iVlanCount"),
        ("TELTONIKA-RUTM-MIB", "iVlanIndex"),
        ("TELTONIKA-RUTM-MIB", "iVlanName"),
        ("TELTONIKA-RUTM-MIB", "iVlanType"),
        ("TELTONIKA-RUTM-MIB", "iVlanIfName"),
        ("TELTONIKA-RUTM-MIB", "iVlanVID"))
)
if mibBuilder.loadTexts:
    iVlanGroup.setStatus("current")

pVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 10)
)
pVlanGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "pVlanCount"),
        ("TELTONIKA-RUTM-MIB", "pVlanIndex"),
        ("TELTONIKA-RUTM-MIB", "pVlanNum"),
        ("TELTONIKA-RUTM-MIB", "pVlanPorts"),
        ("TELTONIKA-RUTM-MIB", "pVlanVID"))
)
if mibBuilder.loadTexts:
    pVlanGroup.setStatus("current")

queueVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 11)
)
queueVlanGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "queueCount"),
        ("TELTONIKA-RUTM-MIB", "queueIndex"),
        ("TELTONIKA-RUTM-MIB", "queueName"),
        ("TELTONIKA-RUTM-MIB", "queueEnabled"),
        ("TELTONIKA-RUTM-MIB", "queueIface"),
        ("TELTONIKA-RUTM-MIB", "queueDownLimit"),
        ("TELTONIKA-RUTM-MIB", "queueUpLimit"),
        ("TELTONIKA-RUTM-MIB", "queueQdisk"),
        ("TELTONIKA-RUTM-MIB", "queueScript"))
)
if mibBuilder.loadTexts:
    queueVlanGroup.setStatus("current")

portGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 12)
)
portGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "portCount"),
        ("TELTONIKA-RUTM-MIB", "pIndex"),
        ("TELTONIKA-RUTM-MIB", "pName"),
        ("TELTONIKA-RUTM-MIB", "pNumber"),
        ("TELTONIKA-RUTM-MIB", "pPosition"),
        ("TELTONIKA-RUTM-MIB", "pState"),
        ("TELTONIKA-RUTM-MIB", "pSpeed"),
        ("TELTONIKA-RUTM-MIB", "pDuplex"))
)
if mibBuilder.loadTexts:
    portGroup.setStatus("current")

mwan3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 12)
)
mwan3Group.setObjects(
      *(("TELTONIKA-RUTM-MIB", "mwan3Count"),
        ("TELTONIKA-RUTM-MIB", "mwan3Index"),
        ("TELTONIKA-RUTM-MIB", "mwan3Name"),
        ("TELTONIKA-RUTM-MIB", "mwan3Enabled"),
        ("TELTONIKA-RUTM-MIB", "mwan3Uptime"),
        ("TELTONIKA-RUTM-MIB", "mwan3Status"),
        ("TELTONIKA-RUTM-MIB", "mwan3Ip"))
)
if mibBuilder.loadTexts:
    mwan3Group.setStatus("current")


# Notification objects

signalChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 1, 1)
)
if mibBuilder.loadTexts:
    signalChangeNotification.setStatus(
        "current"
    )

networkTypeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 1, 2)
)
if mibBuilder.loadTexts:
    networkTypeNotification.setStatus(
        "current"
    )

digitalInputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2, 1)
)
if mibBuilder.loadTexts:
    digitalInputNotification.setStatus(
        "current"
    )

digitalOutputNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2, 2)
)
if mibBuilder.loadTexts:
    digitalOutputNotification.setStatus(
        "current"
    )

clientConnectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 3, 1)
)
if mibBuilder.loadTexts:
    clientConnectedNotification.setStatus(
        "current"
    )

clientDisconnectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 3, 2)
)
if mibBuilder.loadTexts:
    clientDisconnectedNotification.setStatus(
        "current"
    )

eventLogNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 4, 1)
)
if mibBuilder.loadTexts:
    eventLogNotification.setStatus(
        "current"
    )


# Notifications groups

trapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 4)
)
trapGroup.setObjects(
      *(("TELTONIKA-RUTM-MIB", "signalChangeNotification"),
        ("TELTONIKA-RUTM-MIB", "networkTypeNotification"),
        ("TELTONIKA-RUTM-MIB", "digitalInputNotification"),
        ("TELTONIKA-RUTM-MIB", "digitalOutputNotification"),
        ("TELTONIKA-RUTM-MIB", "clientConnectedNotification"),
        ("TELTONIKA-RUTM-MIB", "clientDisconnectedNotification"),
        ("TELTONIKA-RUTM-MIB", "eventLogNotification"))
)
if mibBuilder.loadTexts:
    trapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELTONIKA-RUTM-MIB",
    **{"teltonika": teltonika,
       "teltonikaSnmpGroups": teltonikaSnmpGroups,
       "deviceGroup": deviceGroup,
       "modemGroup": modemGroup,
       "trapGroup": trapGroup,
       "hotspotGroup": hotspotGroup,
       "ioGroup": ioGroup,
       "radioGroup": radioGroup,
       "wIfaceGroup": wIfaceGroup,
       "iVlanGroup": iVlanGroup,
       "pVlanGroup": pVlanGroup,
       "queueVlanGroup": queueVlanGroup,
       "portGroup": portGroup,
       "mwan3Group": mwan3Group,
       "device": device,
       "serial": serial,
       "deviceName": deviceName,
       "productCode": productCode,
       "batchNumber": batchNumber,
       "hardwareRevision": hardwareRevision,
       "fwVersion": fwVersion,
       "deviceUptime": deviceUptime,
       "cpuUsage": cpuUsage,
       "mobile": mobile,
       "modemNum": modemNum,
       "modemTable": modemTable,
       "modemEntry": modemEntry,
       "mIndex": mIndex,
       "mDescr": mDescr,
       "mImei": mImei,
       "mModel": mModel,
       "mManufacturer": mManufacturer,
       "mRevision": mRevision,
       "mSerial": mSerial,
       "mIMSI": mIMSI,
       "mSimState": mSimState,
       "mPinState": mPinState,
       "mNetState": mNetState,
       "mSignal": mSignal,
       "mOperator": mOperator,
       "mOperatorNumber": mOperatorNumber,
       "mConnectionState": mConnectionState,
       "mNetworkType": mNetworkType,
       "mTemperature": mTemperature,
       "mCellID": mCellID,
       "mSINR": mSINR,
       "mRSRP": mRSRP,
       "mRSRQ": mRSRQ,
       "mSent": mSent,
       "mReceived": mReceived,
       "mIP": mIP,
       "mSentToday": mSentToday,
       "mReceivedToday": mReceivedToday,
       "mICCID": mICCID,
       "mSentCurrentWeek": mSentCurrentWeek,
       "mReceivedCurrentWeek": mReceivedCurrentWeek,
       "mSentCurrentMonth": mSentCurrentMonth,
       "mReceivedCurrentMonth": mReceivedCurrentMonth,
       "connectionUptime": connectionUptime,
       "gps": gps,
       "latitude": latitude,
       "longtitude": longtitude,
       "accuracy": accuracy,
       "datetime": datetime,
       "numSatellites": numSatellites,
       "notifications": notifications,
       "mobileNotifications": mobileNotifications,
       "signalChangeNotification": signalChangeNotification,
       "networkTypeNotification": networkTypeNotification,
       "ioNotifications": ioNotifications,
       "digitalInputNotification": digitalInputNotification,
       "digitalOutputNotification": digitalOutputNotification,
       "hotspotNotifications": hotspotNotifications,
       "clientConnectedNotification": clientConnectedNotification,
       "clientDisconnectedNotification": clientDisconnectedNotification,
       "eventNotifications": eventNotifications,
       "eventLogNotification": eventLogNotification,
       "hotspot": hotspot,
       "hsState": hsState,
       "hsIP": hsIP,
       "hsNet": hsNet,
       "hsAuth": hsAuth,
       "hsSessionCount": hsSessionCount,
       "hsSessionTable": hsSessionTable,
       "hsSessionEntry": hsSessionEntry,
       "hssIndex": hssIndex,
       "hssMAC": hssMAC,
       "hssIP": hssIP,
       "hssID": hssID,
       "hssUsername": hssUsername,
       "hssState": hssState,
       "hssDwLimit": hssDwLimit,
       "hssUpLimit": hssUpLimit,
       "hssTimeLimit": hssTimeLimit,
       "hssIdleTimeout": hssIdleTimeout,
       "hssDwBandwidth": hssDwBandwidth,
       "hssUpBandwidth": hssUpBandwidth,
       "hssURL": hssURL,
       "io": io,
       "ioCount": ioCount,
       "ioTable": ioTable,
       "ioEntry": ioEntry,
       "ioIndex": ioIndex,
       "ioSystemName": ioSystemName,
       "ioName": ioName,
       "ioType": ioType,
       "ioBidirectional": ioBidirectional,
       "ioState": ioState,
       "ioInput": ioInput,
       "ioInverted": ioInverted,
       "ioCurrent": ioCurrent,
       "ioPercentage": ioPercentage,
       "ioStateNumeric": ioStateNumeric,
       "wireless": wireless,
       "radioCount": radioCount,
       "radioTable": radioTable,
       "radioEntry": radioEntry,
       "radioIndex": radioIndex,
       "radioName": radioName,
       "radioUpState": radioUpState,
       "radioDisabledState": radioDisabledState,
       "radioChannel": radioChannel,
       "wIfaceCount": wIfaceCount,
       "wIfaceTable": wIfaceTable,
       "wIfaceEntry": wIfaceEntry,
       "wIfaceIndex": wIfaceIndex,
       "wIfaceSSID": wIfaceSSID,
       "wIfaceHidden": wIfaceHidden,
       "wIfaceEncryption": wIfaceEncryption,
       "wIfaceMode": wIfaceMode,
       "vlan": vlan,
       "pVlanCount": pVlanCount,
       "pVlanTable": pVlanTable,
       "pVlanEntry": pVlanEntry,
       "pVlanIndex": pVlanIndex,
       "pVlanNum": pVlanNum,
       "pVlanPorts": pVlanPorts,
       "pVlanVID": pVlanVID,
       "iVlanCount": iVlanCount,
       "iVlanTable": iVlanTable,
       "iVlanEntry": iVlanEntry,
       "iVlanIndex": iVlanIndex,
       "iVlanName": iVlanName,
       "iVlanType": iVlanType,
       "iVlanIfName": iVlanIfName,
       "iVlanVID": iVlanVID,
       "sqm": sqm,
       "queueCount": queueCount,
       "queueTable": queueTable,
       "queueEntry": queueEntry,
       "queueIndex": queueIndex,
       "queueName": queueName,
       "queueEnabled": queueEnabled,
       "queueIface": queueIface,
       "queueDownLimit": queueDownLimit,
       "queueUpLimit": queueUpLimit,
       "queueQdisk": queueQdisk,
       "queueScript": queueScript,
       "port": port,
       "portCount": portCount,
       "portTable": portTable,
       "portEntry": portEntry,
       "pIndex": pIndex,
       "pName": pName,
       "pNumber": pNumber,
       "pPosition": pPosition,
       "pState": pState,
       "pSpeed": pSpeed,
       "pDuplex": pDuplex,
       "mwan3": mwan3,
       "mwan3Count": mwan3Count,
       "mwan3Table": mwan3Table,
       "mwan3Entry": mwan3Entry,
       "mwan3Index": mwan3Index,
       "mwan3Name": mwan3Name,
       "mwan3Enabled": mwan3Enabled,
       "mwan3Uptime": mwan3Uptime,
       "mwan3Status": mwan3Status,
       "mwan3Ip": mwan3Ip}
)
