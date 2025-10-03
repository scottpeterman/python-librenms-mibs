# SNMP MIB module (TELTONIKA-RUTX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teltonika\TELTONIKA-RUTX-MIB
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

teltonika = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48690)
)
if mibBuilder.loadTexts:
    teltonika.setRevisions(
        ("2019-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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


class _RouterName_Type(DisplayString):
    """Custom type routerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RouterName_Type.__name__ = "DisplayString"
_RouterName_Object = MibScalar
routerName = _RouterName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 2),
    _RouterName_Type()
)
routerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerName.setStatus("current")


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
    (0, "TELTONIKA-RUTX-MIB", "mIndex"),
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
_MSignal_Type = Integer32
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


class _MConnectionType_Type(DisplayString):
    """Custom type mConnectionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MConnectionType_Type.__name__ = "DisplayString"
_MConnectionType_Object = MibTableColumn
mConnectionType = _MConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 48690, 2, 2, 1, 16),
    _MConnectionType_Type()
)
mConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mConnectionType.setStatus("current")
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


class _ConnectionUptime_Type(DisplayString):
    """Custom type connectionUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConnectionUptime_Type.__name__ = "DisplayString"
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
_IoNotificationsObs_ObjectIdentity = ObjectIdentity
ioNotificationsObs = _IoNotificationsObs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2, 0)
)


class _DinState_Type(DisplayString):
    """Custom type dinState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DinState_Type.__name__ = "DisplayString"
_DinState_Object = MibScalar
dinState = _DinState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2, 0, 1),
    _DinState_Type()
)
dinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinState.setStatus("current")


class _DoutState_Type(DisplayString):
    """Custom type doutState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DoutState_Type.__name__ = "DisplayString"
_DoutState_Object = MibScalar
doutState = _DoutState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 4, 2, 0, 2),
    _DoutState_Type()
)
doutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doutState.setStatus("current")
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
    (0, "TELTONIKA-RUTX-MIB", "hssIndex"),
)
if mibBuilder.loadTexts:
    hsSessionEntry.setStatus("current")
_HssIndex_Type = Integer32
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
    (0, "TELTONIKA-RUTX-MIB", "ioIndex"),
)
if mibBuilder.loadTexts:
    ioEntry.setStatus("current")
_IoIndex_Type = Integer32
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

# Managed Objects groups


# Notification objects

signalChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 1, 1)
)
if mibBuilder.loadTexts:
    signalChangeNotification.setStatus(
        "current"
    )

connectionTypeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 48690, 4, 1, 2)
)
if mibBuilder.loadTexts:
    connectionTypeNotification.setStatus(
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


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELTONIKA-RUTX-MIB",
    **{"teltonika": teltonika,
       "device": device,
       "serial": serial,
       "routerName": routerName,
       "productCode": productCode,
       "batchNumber": batchNumber,
       "hardwareRevision": hardwareRevision,
       "fwVersion": fwVersion,
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
       "mConnectionType": mConnectionType,
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
       "connectionTypeNotification": connectionTypeNotification,
       "ioNotifications": ioNotifications,
       "ioNotificationsObs": ioNotificationsObs,
       "dinState": dinState,
       "doutState": doutState,
       "digitalInputNotification": digitalInputNotification,
       "digitalOutputNotification": digitalOutputNotification,
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
       "ioPercentage": ioPercentage}
)
