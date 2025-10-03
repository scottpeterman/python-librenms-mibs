# SNMP MIB module (IPO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avaya\IPO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:05 2025
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

(mibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "mibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ipoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2)
)
if mibBuilder.loadTexts:
    ipoMIB.setRevisions(
        ("2014-07-04 00:00",
         "2014-06-25 00:00",
         "2014-06-25 00:00",
         "2014-06-16 00:00",
         "2014-06-04 00:00",
         "2014-05-23 00:00",
         "2014-05-08 00:00",
         "2014-01-06 00:00",
         "2013-10-08 00:00",
         "2013-08-06 00:00",
         "2013-04-24 19:00",
         "2013-04-24 15:18",
         "2012-11-17 15:11",
         "2012-02-28 13:00",
         "2011-11-01 22:00",
         "2011-09-27 11:30",
         "2011-03-15 15:17",
         "2010-10-13 14:17",
         "2010-07-12 13:45",
         "2009-10-19 07:35",
         "2009-10-09 13:47",
         "2009-09-11 09:50",
         "2009-09-07 16:20",
         "2008-04-28 16:40",
         "2008-04-18 14:50",
         "2006-06-29 00:00",
         "2004-10-06 00:00",
         "2004-08-27 00:00",
         "2004-08-06 00:00",
         "2004-07-10 00:00",
         "2004-05-28 00:00",
         "2004-03-03 00:00",
         "2003-12-15 00:00",
         "2003-11-11 00:00",
         "2003-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpoGeneric_ObjectIdentity = ObjectIdentity
ipoGeneric = _IpoGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1)
)
_IpoGenMibs_ObjectIdentity = ObjectIdentity
ipoGenMibs = _IpoGenMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1)
)
_IpoGenTraps_ObjectIdentity = ObjectIdentity
ipoGenTraps = _IpoGenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2)
)
_IpoGTEvents_ObjectIdentity = ObjectIdentity
ipoGTEvents = _IpoGTEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0)
)
_IpoGTObjects_ObjectIdentity = ObjectIdentity
ipoGTObjects = _IpoGTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1)
)


class _IpoGTEventSeverity_Type(Integer32):
    """Custom type ipoGTEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_IpoGTEventSeverity_Type.__name__ = "Integer32"
_IpoGTEventSeverity_Object = MibScalar
ipoGTEventSeverity = _IpoGTEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 1),
    _IpoGTEventSeverity_Type()
)
ipoGTEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventSeverity.setStatus("deprecated")
_IpoGTEventDateTime_Type = DateAndTime
_IpoGTEventDateTime_Object = MibScalar
ipoGTEventDateTime = _IpoGTEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 2),
    _IpoGTEventDateTime_Type()
)
ipoGTEventDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventDateTime.setStatus("current")
_IpoGTEventEntity_Type = Unsigned32
_IpoGTEventEntity_Object = MibScalar
ipoGTEventEntity = _IpoGTEventEntity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 3),
    _IpoGTEventEntity_Type()
)
ipoGTEventEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventEntity.setStatus("current")


class _IpoGTEventLoopbackStatus_Type(Integer32):
    """Custom type ipoGTEventLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_IpoGTEventLoopbackStatus_Type.__name__ = "Integer32"
_IpoGTEventLoopbackStatus_Object = MibScalar
ipoGTEventLoopbackStatus = _IpoGTEventLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 4),
    _IpoGTEventLoopbackStatus_Type()
)
ipoGTEventLoopbackStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventLoopbackStatus.setStatus("deprecated")


class _IpoGTEventAppEntity_Type(Integer32):
    """Custom type ipoGTEventAppEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("voiceMail", 1),
          ("deltaServer", 2),
          ("customerCallReporter", 3),
          ("oneXPortal", 4))
    )


_IpoGTEventAppEntity_Type.__name__ = "Integer32"
_IpoGTEventAppEntity_Object = MibScalar
ipoGTEventAppEntity = _IpoGTEventAppEntity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 5),
    _IpoGTEventAppEntity_Type()
)
ipoGTEventAppEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventAppEntity.setStatus("current")


class _IpoGTEventAppEvent_Type(Integer32):
    """Custom type ipoGTEventAppEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73)
        )
    )
    namedValues = NamedValues(
        *(("storageFull", 1),
          ("storageNearlyFull", 2),
          ("storageOkay", 3),
          ("backupCommunicationError", 4),
          ("backupFileError", 5),
          ("httpFailure", 6),
          ("httpSslAcceptFailure", 7),
          ("httpSslConnection", 8),
          ("httpSslFailure", 9),
          ("httpSslPortFailure", 10),
          ("ignoringRequest", 11),
          ("imapInitializationFailed", 12),
          ("imapInvalidMsgNr", 13),
          ("imapMailboxNotExist", 14),
          ("imapMessageInvalid", 15),
          ("imapMessageNotExist", 16),
          ("imapMessageNrNotExist", 17),
          ("imapMissingConnection", 18),
          ("imapMissingSettings", 19),
          ("imapNoLicence", 20),
          ("imapNotConfigured", 21),
          ("imapShiftConnection", 22),
          ("mapiInitializationFailed", 23),
          ("mapiMissingSettings", 24),
          ("mapiConnectionFailed", 25),
          ("mapiShiftConnection", 26),
          ("licence", 27),
          ("licenceDistributed", 28),
          ("licenceExpired", 29),
          ("licenceSOG", 30),
          ("loginFailure", 31),
          ("loginFailureInvalidMailbox", 32),
          ("mailboxNotFound", 33),
          ("makeLiveFileAccess", 34),
          ("makeLiveMissingFile", 35),
          ("offlineMakeLive", 36),
          ("onexError", 37),
          ("pbxConnectionLost", 38),
          ("pbxIncompatibility", 39),
          ("smgrSettingsError", 40),
          ("smtpConnectionFailed", 41),
          ("smtpConnectionTimeout", 42),
          ("smtpError", 43),
          ("smtpSecureConnectionFailed", 44),
          ("smtpUnexpectedData", 45),
          ("smtpUnsuportedData", 46),
          ("socketAbortingError", 47),
          ("socketBindError", 48),
          ("socketClientDisconnectedError", 49),
          ("socketConnectionError", 50),
          ("socketNoresponseError", 51),
          ("socketOptionError", 52),
          ("socketReceiveError", 53),
          ("socketRecvFailedError", 54),
          ("socketSendFailedError", 55),
          ("socketSelectError", 56),
          ("socketTimedOutError", 57),
          ("switchedToPrimary", 58),
          ("switchedToSecondary", 59),
          ("tcpAcceptError", 60),
          ("tcpListenError", 61),
          ("tcpSelectError", 62),
          ("tcpError", 63),
          ("testTimeExpired", 64),
          ("tftpConnectionError", 65),
          ("tftpMonitoringError", 66),
          ("tftpReadingError", 67),
          ("tftpReceivingError", 68),
          ("tftpWrittingError", 69),
          ("tooManyClients", 70),
          ("updateEerror", 71),
          ("updateSuccess", 72),
          ("vmScript", 73))
    )


_IpoGTEventAppEvent_Type.__name__ = "Integer32"
_IpoGTEventAppEvent_Object = MibScalar
ipoGTEventAppEvent = _IpoGTEventAppEvent_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 6),
    _IpoGTEventAppEvent_Type()
)
ipoGTEventAppEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventAppEvent.setStatus("current")
_IpoGTEventHostAddress_Type = IpAddress
_IpoGTEventHostAddress_Object = MibScalar
ipoGTEventHostAddress = _IpoGTEventHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 7),
    _IpoGTEventHostAddress_Type()
)
ipoGTEventHostAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventHostAddress.setStatus("current")


class _IpoGTEventSOGMode_Type(Integer32):
    """Custom type ipoGTEventSOGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("survivable", 1),
          ("subTending", 2))
    )


_IpoGTEventSOGMode_Type.__name__ = "Integer32"
_IpoGTEventSOGMode_Object = MibScalar
ipoGTEventSOGMode = _IpoGTEventSOGMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 8),
    _IpoGTEventSOGMode_Type()
)
ipoGTEventSOGMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventSOGMode.setStatus("current")
_IpoGTEventStdSeverity_Type = ItuPerceivedSeverity
_IpoGTEventStdSeverity_Object = MibScalar
ipoGTEventStdSeverity = _IpoGTEventStdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 9),
    _IpoGTEventStdSeverity_Type()
)
ipoGTEventStdSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventStdSeverity.setStatus("current")


class _IpoGTEventDevID_Type(SnmpAdminString):
    """Custom type ipoGTEventDevID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_IpoGTEventDevID_Type.__name__ = "SnmpAdminString"
_IpoGTEventDevID_Object = MibScalar
ipoGTEventDevID = _IpoGTEventDevID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 10),
    _IpoGTEventDevID_Type()
)
ipoGTEventDevID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventDevID.setStatus("current")


class _IpoGTEventEntityName_Type(SnmpAdminString):
    """Custom type ipoGTEventEntityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IpoGTEventEntityName_Type.__name__ = "SnmpAdminString"
_IpoGTEventEntityName_Object = MibScalar
ipoGTEventEntityName = _IpoGTEventEntityName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 11),
    _IpoGTEventEntityName_Type()
)
ipoGTEventEntityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventEntityName.setStatus("current")


class _IpoGTEventLoopbackStatusBits_Type(Bits):
    """Custom type ipoGTEventLoopbackStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("noLoopback", 0),
          ("nearEndPayloadLoopback", 1),
          ("nearEndLineLoopback", 2),
          ("nearEndOtherLoopback", 3),
          ("nearEndInwardLoopback", 4),
          ("farEndPayloadLoopback", 5),
          ("farEndLineLoopback", 6))
    )

_IpoGTEventLoopbackStatusBits_Type.__name__ = "Bits"
_IpoGTEventLoopbackStatusBits_Object = MibScalar
ipoGTEventLoopbackStatusBits = _IpoGTEventLoopbackStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 12),
    _IpoGTEventLoopbackStatusBits_Type()
)
ipoGTEventLoopbackStatusBits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventLoopbackStatusBits.setStatus("current")
_IpoGTEventQoSMonJitter_Type = Unsigned32
_IpoGTEventQoSMonJitter_Object = MibScalar
ipoGTEventQoSMonJitter = _IpoGTEventQoSMonJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 13),
    _IpoGTEventQoSMonJitter_Type()
)
ipoGTEventQoSMonJitter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonJitter.setStatus("current")
_IpoGTEventQoSMonRndTrip_Type = Unsigned32
_IpoGTEventQoSMonRndTrip_Object = MibScalar
ipoGTEventQoSMonRndTrip = _IpoGTEventQoSMonRndTrip_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 14),
    _IpoGTEventQoSMonRndTrip_Type()
)
ipoGTEventQoSMonRndTrip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonRndTrip.setStatus("current")
_IpoGTEventQoSMonPktLoss_Type = Unsigned32
_IpoGTEventQoSMonPktLoss_Object = MibScalar
ipoGTEventQoSMonPktLoss = _IpoGTEventQoSMonPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 15),
    _IpoGTEventQoSMonPktLoss_Type()
)
ipoGTEventQoSMonPktLoss.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonPktLoss.setStatus("current")
_IpoGTEventQoSMonCallId_Type = Unsigned32
_IpoGTEventQoSMonCallId_Object = MibScalar
ipoGTEventQoSMonCallId = _IpoGTEventQoSMonCallId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 16),
    _IpoGTEventQoSMonCallId_Type()
)
ipoGTEventQoSMonCallId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonCallId.setStatus("current")


class _IpoGTEventQoSMonDevType_Type(Integer32):
    """Custom type ipoGTEventQoSMonDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("extn", 2))
    )


_IpoGTEventQoSMonDevType_Type.__name__ = "Integer32"
_IpoGTEventQoSMonDevType_Object = MibScalar
ipoGTEventQoSMonDevType = _IpoGTEventQoSMonDevType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 17),
    _IpoGTEventQoSMonDevType_Type()
)
ipoGTEventQoSMonDevType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonDevType.setStatus("current")
_IpoGTEventQoSMonDevId_Type = Unsigned32
_IpoGTEventQoSMonDevId_Object = MibScalar
ipoGTEventQoSMonDevId = _IpoGTEventQoSMonDevId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 18),
    _IpoGTEventQoSMonDevId_Type()
)
ipoGTEventQoSMonDevId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonDevId.setStatus("current")
_IpoGTEventQoSMonExtnNo_Type = Unsigned32
_IpoGTEventQoSMonExtnNo_Object = MibScalar
ipoGTEventQoSMonExtnNo = _IpoGTEventQoSMonExtnNo_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 19),
    _IpoGTEventQoSMonExtnNo_Type()
)
ipoGTEventQoSMonExtnNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventQoSMonExtnNo.setStatus("current")


class _IpoGTEventSystemShutdownSource_Type(SnmpAdminString):
    """Custom type ipoGTEventSystemShutdownSource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpoGTEventSystemShutdownSource_Type.__name__ = "SnmpAdminString"
_IpoGTEventSystemShutdownSource_Object = MibScalar
ipoGTEventSystemShutdownSource = _IpoGTEventSystemShutdownSource_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 20),
    _IpoGTEventSystemShutdownSource_Type()
)
ipoGTEventSystemShutdownSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventSystemShutdownSource.setStatus("current")
_IpoGTEventSystemShutdownTimeout_Type = Unsigned32
_IpoGTEventSystemShutdownTimeout_Object = MibScalar
ipoGTEventSystemShutdownTimeout = _IpoGTEventSystemShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 21),
    _IpoGTEventSystemShutdownTimeout_Type()
)
ipoGTEventSystemShutdownTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventSystemShutdownTimeout.setStatus("current")


class _IpoGTEventMemoryCardSlotId_Type(Integer32):
    """Custom type ipoGTEventMemoryCardSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compactFlash", 1),
          ("systemSD", 2),
          ("optionalSD", 3))
    )


_IpoGTEventMemoryCardSlotId_Type.__name__ = "Integer32"
_IpoGTEventMemoryCardSlotId_Object = MibScalar
ipoGTEventMemoryCardSlotId = _IpoGTEventMemoryCardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 22),
    _IpoGTEventMemoryCardSlotId_Type()
)
ipoGTEventMemoryCardSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventMemoryCardSlotId.setStatus("current")


class _IpoGTEventNoValidKeyReason_Type(Integer32):
    """Custom type ipoGTEventNoValidKeyReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noReason", 1),
          ("notPresent", 2),
          ("noRegisterAccess", 3),
          ("invalidRegisters", 4),
          ("invalidWatermark", 5),
          ("invalidClusterSize", 6),
          ("invalidVolume", 7),
          ("invalidHeaderFiles", 8),
          ("nonSpecificError", 9))
    )


_IpoGTEventNoValidKeyReason_Type.__name__ = "Integer32"
_IpoGTEventNoValidKeyReason_Object = MibScalar
ipoGTEventNoValidKeyReason = _IpoGTEventNoValidKeyReason_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 23),
    _IpoGTEventNoValidKeyReason_Type()
)
ipoGTEventNoValidKeyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventNoValidKeyReason.setStatus("current")


class _IpoGTEventReason_Type(Integer32):
    """Custom type ipoGTEventReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79)
        )
    )
    namedValues = NamedValues(
        *(("configurationAgentNotTargeted", 1),
          ("configurationSCNDialPlanConflict", 2),
          ("configurationNoIncomingCallRoute", 3),
          ("configurationHWTypeFailure", 4),
          ("serviceFeatureLicenseMissing", 5),
          ("serviceAllLicensesInUse", 6),
          ("serviceClockSourceChanged", 7),
          ("serviceLogonFailed", 8),
          ("serviceNoFreeChannelsAvail", 9),
          ("serviceHoldMusicFileFailure", 10),
          ("serviceAllResourcesInUse", 11),
          ("serviceAlarm", 12),
          ("serviceNetworkInterconnectFailure", 13),
          ("trunkSeizeFailure", 14),
          ("trunkIncomingCallOutgoingTrunk", 15),
          ("trunkCLINotDelivered", 16),
          ("trunkDDIIncomplete", 17),
          ("trunkLOS", 18),
          ("trunkOOS", 19),
          ("trunkRedAlarm", 20),
          ("trunkBlueAlarm", 21),
          ("trunkYellowAlarm", 22),
          ("trunkIPConnectFail", 23),
          ("trunkSCNInvalidConnection", 24),
          ("linkDeviceChanged", 25),
          ("linkLDAPServerCommFailure", 26),
          ("linkResourceDown", 27),
          ("linkSMTPServerCommFailure", 28),
          ("linkVMProConnFailure", 29),
          ("serviceTimeServerAlarm", 30),
          ("serviceLicenseFileInvalid", 31),
          ("serviceLicenseError", 32),
          ("securityError", 33),
          ("codecError", 34),
          ("scepNoRespError", 35),
          ("configAppsProcAlarm", 36),
          ("serviceAppsProcAlarm", 37),
          ("serviceLicenseServerError", 38),
          ("testAlarm", 39),
          ("servicePlannedMaintenance", 40),
          ("serviceNetworkDisconnection", 41),
          ("serviceFailedTlsNegotiation", 42),
          ("serviceFailedTlsRenegotiation", 43),
          ("serviceLackOfResources", 44),
          ("serviceInternalError", 45),
          ("serviceTooManyMissedHeartbeats", 46),
          ("serviceFailedDnsResolution", 47),
          ("serviceDuplicateIpAddress", 48),
          ("serviceAuthenticationFailure", 49),
          ("serviceSslVpnStackProtocolError", 50),
          ("serviceSslVpnServerReportedError", 51),
          ("servicePortRangeExhausted", 52),
          ("serviceWebservicesUWSError", 53),
          ("trunkNoFreeVoIPChannel", 54),
          ("serviceEmergencyCall", 55),
          ("serviceLocationCongestion", 56),
          ("serviceCpuAlarm", 57),
          ("serviceCpuIOAlarm", 58),
          ("serviceMemoryAlarm", 59),
          ("serviceLocalBackup", 60),
          ("trunkSMConnectAsSIP", 61),
          ("trunkSIPConnectAsSM", 62),
          ("serviceSipRxPacketSizeError", 63),
          ("serviceACCSAlarm", 64),
          ("serviceSystemHardDriveAlarm", 65),
          ("serviceAdditionalHardDriveAlarm", 66),
          ("linkDialerConnFailure", 67),
          ("trunkSIPDNSInvalidConfig", 68),
          ("trunkSIPDNSTransportError", 69),
          ("monitorLogStamped", 70),
          ("trunkSCNInvalidSubOperMode", 71),
          ("serviceIPDECTSystemError", 72),
          ("serviceIPOCCAlarm", 73),
          ("serviceGeneralAlarm", 74),
          ("serviceSystemInfo", 75),
          ("serviceNonSelectAlarm", 76),
          ("serviceCCRNotSupported", 77),
          ("serviceAMServerNotAvailable", 78),
          ("trunkMediaSecuritySettingsIncompatible", 79))
    )


_IpoGTEventReason_Type.__name__ = "Integer32"
_IpoGTEventReason_Object = MibScalar
ipoGTEventReason = _IpoGTEventReason_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 24),
    _IpoGTEventReason_Type()
)
ipoGTEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventReason.setStatus("current")


class _IpoGTEventData_Type(SnmpAdminString):
    """Custom type ipoGTEventData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpoGTEventData_Type.__name__ = "SnmpAdminString"
_IpoGTEventData_Object = MibScalar
ipoGTEventData = _IpoGTEventData_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 25),
    _IpoGTEventData_Type()
)
ipoGTEventData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventData.setStatus("current")


class _IpoGTEventAlarmDescription_Type(SnmpAdminString):
    """Custom type ipoGTEventAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpoGTEventAlarmDescription_Type.__name__ = "SnmpAdminString"
_IpoGTEventAlarmDescription_Object = MibScalar
ipoGTEventAlarmDescription = _IpoGTEventAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 26),
    _IpoGTEventAlarmDescription_Type()
)
ipoGTEventAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventAlarmDescription.setStatus("current")


class _IpoGTEventAlarmRemedialAction_Type(SnmpAdminString):
    """Custom type ipoGTEventAlarmRemedialAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpoGTEventAlarmRemedialAction_Type.__name__ = "SnmpAdminString"
_IpoGTEventAlarmRemedialAction_Object = MibScalar
ipoGTEventAlarmRemedialAction = _IpoGTEventAlarmRemedialAction_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 1, 27),
    _IpoGTEventAlarmRemedialAction_Type()
)
ipoGTEventAlarmRemedialAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipoGTEventAlarmRemedialAction.setStatus("current")
_IpoGenConformance_ObjectIdentity = ObjectIdentity
ipoGenConformance = _IpoGenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3)
)
_IpoGenCompliances_ObjectIdentity = ObjectIdentity
ipoGenCompliances = _IpoGenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1)
)
_IpoGenGroups_ObjectIdentity = ObjectIdentity
ipoGenGroups = _IpoGenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2)
)

# Managed Objects groups

ipoGenNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 1)
)
ipoGenNotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventLoopbackStatus"),
        ("IPO-MIB", "ipoGTEventAppEntity"),
        ("IPO-MIB", "ipoGTEventAppEvent"))
)
if mibBuilder.loadTexts:
    ipoGenNotificationObjectsGroup.setStatus("deprecated")

ipoGenSOGNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 3)
)
ipoGenSOGNotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventHostAddress"),
        ("IPO-MIB", "ipoGTEventSOGMode"))
)
if mibBuilder.loadTexts:
    ipoGenSOGNotificationObjectsGroup.setStatus("current")

ipoGenv2NotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 5)
)
ipoGenv2NotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventAppEntity"),
        ("IPO-MIB", "ipoGTEventAppEvent"),
        ("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("IPO-MIB", "ipoGTEventEntityName"),
        ("IPO-MIB", "ipoGTEventLoopbackStatusBits"))
)
if mibBuilder.loadTexts:
    ipoGenv2NotificationObjectsGroup.setStatus("current")

ipoGenQosMonNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 10)
)
ipoGenQosMonNotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventQoSMonJitter"),
        ("IPO-MIB", "ipoGTEventQoSMonRndTrip"),
        ("IPO-MIB", "ipoGTEventQoSMonPktLoss"),
        ("IPO-MIB", "ipoGTEventQoSMonCallId"),
        ("IPO-MIB", "ipoGTEventQoSMonDevType"),
        ("IPO-MIB", "ipoGTEventQoSMonDevId"),
        ("IPO-MIB", "ipoGTEventQoSMonExtnNo"))
)
if mibBuilder.loadTexts:
    ipoGenQosMonNotificationObjectsGroup.setStatus("current")

ipoGenSvcSystemShutdownObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 12)
)
ipoGenSvcSystemShutdownObjectGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventSystemShutdownSource"),
        ("IPO-MIB", "ipoGTEventSystemShutdownTimeout"))
)
if mibBuilder.loadTexts:
    ipoGenSvcSystemShutdownObjectGroup.setStatus("current")

ipoGenSDcardNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 14)
)
ipoGenSDcardNotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventMemoryCardSlotId"),
        ("IPO-MIB", "ipoGTEventNoValidKeyReason"))
)
if mibBuilder.loadTexts:
    ipoGenSDcardNotificationObjectsGroup.setStatus("current")

ipoGenSvcMiscNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 16)
)
ipoGenSvcMiscNotificationObjectsGroup.setObjects(
      *(("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenSvcMiscNotificationObjectsGroup.setStatus("current")


# Notification objects

ipoGenEntityFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 1)
)
ipoGenEntityFailureEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"))
)
if mibBuilder.loadTexts:
    ipoGenEntityFailureEvent.setStatus(
        "deprecated"
    )

ipoGenEntityOperationalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 2)
)
ipoGenEntityOperationalEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"))
)
if mibBuilder.loadTexts:
    ipoGenEntityOperationalEvent.setStatus(
        "deprecated"
    )

ipoGenEntityErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 3)
)
ipoGenEntityErrorEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"))
)
if mibBuilder.loadTexts:
    ipoGenEntityErrorEvent.setStatus(
        "deprecated"
    )

ipoGenEntityChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 4)
)
ipoGenEntityChangeEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"))
)
if mibBuilder.loadTexts:
    ipoGenEntityChangeEvent.setStatus(
        "deprecated"
    )

ipoGenLKSCommsFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 5)
)
ipoGenLKSCommsFailureEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsFailureEvent.setStatus(
        "deprecated"
    )

ipoGenLKSCommsOperationalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 6)
)
ipoGenLKSCommsOperationalEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsOperationalEvent.setStatus(
        "deprecated"
    )

ipoGenLKSCommsErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 7)
)
ipoGenLKSCommsErrorEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsErrorEvent.setStatus(
        "deprecated"
    )

ipoGenLKSCommsChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 8)
)
ipoGenLKSCommsChangeEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsChangeEvent.setStatus(
        "deprecated"
    )

ipoGenLoopbackEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 9)
)
ipoGenLoopbackEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventLoopbackStatus"))
)
if mibBuilder.loadTexts:
    ipoGenLoopbackEvent.setStatus(
        "deprecated"
    )

ipoGenAppFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 10)
)
ipoGenAppFailureEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventAppEntity"))
)
if mibBuilder.loadTexts:
    ipoGenAppFailureEvent.setStatus(
        "deprecated"
    )

ipoGenAppOperationalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 11)
)
ipoGenAppOperationalEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventAppEntity"))
)
if mibBuilder.loadTexts:
    ipoGenAppOperationalEvent.setStatus(
        "deprecated"
    )

ipoGenAppEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 12)
)
ipoGenAppEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventAppEntity"),
        ("IPO-MIB", "ipoGTEventAppEvent"))
)
if mibBuilder.loadTexts:
    ipoGenAppEvent.setStatus(
        "deprecated"
    )

ipoGenSogHostFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 13)
)
ipoGenSogHostFailureEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventHostAddress"))
)
if mibBuilder.loadTexts:
    ipoGenSogHostFailureEvent.setStatus(
        "deprecated"
    )

ipoGenSogModeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 14)
)
ipoGenSogModeChangeEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventSOGMode"))
)
if mibBuilder.loadTexts:
    ipoGenSogModeChangeEvent.setStatus(
        "deprecated"
    )

ipoGenColdStartSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 15)
)
ipoGenColdStartSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenColdStartSvcEvent.setStatus(
        "current"
    )

ipoGenWarmStartSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 16)
)
ipoGenWarmStartSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenWarmStartSvcEvent.setStatus(
        "current"
    )

ipoGenLinkDownSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 17)
)
ipoGenLinkDownSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    ipoGenLinkDownSvcEvent.setStatus(
        "current"
    )

ipoGenLinkUpSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 18)
)
ipoGenLinkUpSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    ipoGenLinkUpSvcEvent.setStatus(
        "current"
    )

ipoGenAuthFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 19)
)
ipoGenAuthFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenAuthFailureSvcEvent.setStatus(
        "current"
    )

ipoGenEntityFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 20)
)
ipoGenEntityFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventEntityName"))
)
if mibBuilder.loadTexts:
    ipoGenEntityFailureSvcEvent.setStatus(
        "current"
    )

ipoGenEntityOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 21)
)
ipoGenEntityOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventEntityName"))
)
if mibBuilder.loadTexts:
    ipoGenEntityOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenEntityErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 22)
)
ipoGenEntityErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventEntityName"))
)
if mibBuilder.loadTexts:
    ipoGenEntityErrorSvcEvent.setStatus(
        "current"
    )

ipoGenEntityChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 23)
)
ipoGenEntityChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventEntityName"))
)
if mibBuilder.loadTexts:
    ipoGenEntityChangeSvcEvent.setStatus(
        "current"
    )

ipoGenLKSCommsFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 24)
)
ipoGenLKSCommsFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsFailureSvcEvent.setStatus(
        "current"
    )

ipoGenLKSCommsOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 25)
)
ipoGenLKSCommsOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenLKSCommsErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 26)
)
ipoGenLKSCommsErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsErrorSvcEvent.setStatus(
        "current"
    )

ipoGenLKSCommsChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 27)
)
ipoGenLKSCommsChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenLKSCommsChangeSvcEvent.setStatus(
        "current"
    )

ipoGenLoopbackSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 28)
)
ipoGenLoopbackSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventEntity"),
        ("IPO-MIB", "ipoGTEventEntityName"),
        ("IPO-MIB", "ipoGTEventLoopbackStatusBits"))
)
if mibBuilder.loadTexts:
    ipoGenLoopbackSvcEvent.setStatus(
        "current"
    )

ipoGenAppFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 29)
)
ipoGenAppFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventAppEntity"))
)
if mibBuilder.loadTexts:
    ipoGenAppFailureSvcEvent.setStatus(
        "current"
    )

ipoGenAppOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 30)
)
ipoGenAppOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventAppEntity"))
)
if mibBuilder.loadTexts:
    ipoGenAppOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenAppSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 31)
)
ipoGenAppSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventAppEntity"),
        ("IPO-MIB", "ipoGTEventAppEvent"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"))
)
if mibBuilder.loadTexts:
    ipoGenAppSvcEvent.setStatus(
        "current"
    )

ipoGenSogHostFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 32)
)
ipoGenSogHostFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventHostAddress"))
)
if mibBuilder.loadTexts:
    ipoGenSogHostFailureSvcEvent.setStatus(
        "current"
    )

ipoGenSogModeChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 33)
)
ipoGenSogModeChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventSOGMode"))
)
if mibBuilder.loadTexts:
    ipoGenSogModeChangeSvcEvent.setStatus(
        "current"
    )

ipoGenUPriLicChansReducedSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 34)
)
ipoGenUPriLicChansReducedSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenUPriLicChansReducedSvcEvent.setStatus(
        "current"
    )

ipoGenUPriLicCallRejectedSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 35)
)
ipoGenUPriLicCallRejectedSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenUPriLicCallRejectedSvcEvent.setStatus(
        "current"
    )

ipoGenQoSMonSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 36)
)
ipoGenQoSMonSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventQoSMonJitter"),
        ("IPO-MIB", "ipoGTEventQoSMonRndTrip"),
        ("IPO-MIB", "ipoGTEventQoSMonPktLoss"),
        ("IPO-MIB", "ipoGTEventQoSMonCallId"),
        ("IPO-MIB", "ipoGTEventQoSMonDevType"),
        ("IPO-MIB", "ipoGTEventQoSMonDevId"),
        ("IPO-MIB", "ipoGTEventQoSMonExtnNo"))
)
if mibBuilder.loadTexts:
    ipoGenQoSMonSvcEvent.setStatus(
        "current"
    )

ipoGenSystemShutdownSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 37)
)
ipoGenSystemShutdownSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventSystemShutdownSource"),
        ("IPO-MIB", "ipoGTEventSystemShutdownTimeout"))
)
if mibBuilder.loadTexts:
    ipoGenSystemShutdownSvcEvent.setStatus(
        "current"
    )

ipoGenSystemRunningBackupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 38)
)
ipoGenSystemRunningBackupEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    ipoGenSystemRunningBackupEvent.setStatus(
        "current"
    )

ipoGenInvalidMemoryCardEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 39)
)
ipoGenInvalidMemoryCardEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventMemoryCardSlotId"))
)
if mibBuilder.loadTexts:
    ipoGenInvalidMemoryCardEvent.setStatus(
        "current"
    )

ipoGenNoLicenceKeyDongleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 40)
)
ipoGenNoLicenceKeyDongleEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventNoValidKeyReason"))
)
if mibBuilder.loadTexts:
    ipoGenNoLicenceKeyDongleEvent.setStatus(
        "current"
    )

ipoGenMemoryCardCapacityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 41)
)
ipoGenMemoryCardCapacityEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventMemoryCardSlotId"),
        ("IPO-MIB", "ipoGTEventAppEvent"))
)
if mibBuilder.loadTexts:
    ipoGenMemoryCardCapacityEvent.setStatus(
        "current"
    )

ipoGenConfigFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 42)
)
ipoGenConfigFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenConfigFailureSvcEvent.setStatus(
        "current"
    )

ipoGenConfigOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 43)
)
ipoGenConfigOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"))
)
if mibBuilder.loadTexts:
    ipoGenConfigOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenConfigErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 44)
)
ipoGenConfigErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenConfigErrorSvcEvent.setStatus(
        "current"
    )

ipoGenConfigChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 45)
)
ipoGenConfigChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenConfigChangeSvcEvent.setStatus(
        "current"
    )

ipoGenServiceFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 46)
)
ipoGenServiceFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenServiceFailureSvcEvent.setStatus(
        "current"
    )

ipoGenServiceOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 47)
)
ipoGenServiceOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"))
)
if mibBuilder.loadTexts:
    ipoGenServiceOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenServiceErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 48)
)
ipoGenServiceErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenServiceErrorSvcEvent.setStatus(
        "current"
    )

ipoGenServiceChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 49)
)
ipoGenServiceChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenServiceChangeSvcEvent.setStatus(
        "current"
    )

ipoGenTrunkFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 50)
)
ipoGenTrunkFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenTrunkFailureSvcEvent.setStatus(
        "current"
    )

ipoGenTrunkOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 51)
)
ipoGenTrunkOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"))
)
if mibBuilder.loadTexts:
    ipoGenTrunkOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenTrunkErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 52)
)
ipoGenTrunkErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenTrunkErrorSvcEvent.setStatus(
        "current"
    )

ipoGenTrunkChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 53)
)
ipoGenTrunkChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenTrunkChangeSvcEvent.setStatus(
        "current"
    )

ipoGenLinkFailureSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 54)
)
ipoGenLinkFailureSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenLinkFailureSvcEvent.setStatus(
        "current"
    )

ipoGenLinkOperationalSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 55)
)
ipoGenLinkOperationalSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"))
)
if mibBuilder.loadTexts:
    ipoGenLinkOperationalSvcEvent.setStatus(
        "current"
    )

ipoGenLinkErrorSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 56)
)
ipoGenLinkErrorSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenLinkErrorSvcEvent.setStatus(
        "current"
    )

ipoGenLinkChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 57)
)
ipoGenLinkChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenLinkChangeSvcEvent.setStatus(
        "current"
    )

ipoGenEmergencyCallSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 2, 0, 58)
)
ipoGenEmergencyCallSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-MIB", "ipoGTEventReason"),
        ("IPO-MIB", "ipoGTEventData"),
        ("IPO-MIB", "ipoGTEventAlarmDescription"),
        ("IPO-MIB", "ipoGTEventAlarmRemedialAction"))
)
if mibBuilder.loadTexts:
    ipoGenEmergencyCallSvcEvent.setStatus(
        "current"
    )


# Notifications groups

ipoGenNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 2)
)
ipoGenNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenEntityFailureEvent"),
        ("IPO-MIB", "ipoGenEntityOperationalEvent"),
        ("IPO-MIB", "ipoGenEntityErrorEvent"),
        ("IPO-MIB", "ipoGenEntityChangeEvent"),
        ("IPO-MIB", "ipoGenLKSCommsFailureEvent"),
        ("IPO-MIB", "ipoGenLKSCommsOperationalEvent"),
        ("IPO-MIB", "ipoGenLKSCommsErrorEvent"),
        ("IPO-MIB", "ipoGenLKSCommsChangeEvent"),
        ("IPO-MIB", "ipoGenLoopbackEvent"),
        ("IPO-MIB", "ipoGenAppOperationalEvent"),
        ("IPO-MIB", "ipoGenAppFailureEvent"),
        ("IPO-MIB", "ipoGenAppEvent"))
)
if mibBuilder.loadTexts:
    ipoGenNotificationsGroup.setStatus(
        "deprecated"
    )

ipoGenSOGNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 4)
)
ipoGenSOGNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenSogHostFailureEvent"),
        ("IPO-MIB", "ipoGenSogModeChangeEvent"))
)
if mibBuilder.loadTexts:
    ipoGenSOGNotificationsGroup.setStatus(
        "deprecated"
    )

ipoGenEntGenNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 6)
)
ipoGenEntGenNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenColdStartSvcEvent"),
        ("IPO-MIB", "ipoGenWarmStartSvcEvent"),
        ("IPO-MIB", "ipoGenLinkDownSvcEvent"),
        ("IPO-MIB", "ipoGenLinkUpSvcEvent"),
        ("IPO-MIB", "ipoGenAuthFailureSvcEvent"))
)
if mibBuilder.loadTexts:
    ipoGenEntGenNotificationsGroup.setStatus(
        "current"
    )

ipoGenSvcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 7)
)
ipoGenSvcNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenEntityFailureSvcEvent"),
        ("IPO-MIB", "ipoGenEntityOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenEntityErrorSvcEvent"),
        ("IPO-MIB", "ipoGenEntityChangeSvcEvent"),
        ("IPO-MIB", "ipoGenLKSCommsFailureSvcEvent"),
        ("IPO-MIB", "ipoGenLKSCommsOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenLKSCommsErrorSvcEvent"),
        ("IPO-MIB", "ipoGenLKSCommsChangeSvcEvent"),
        ("IPO-MIB", "ipoGenLoopbackSvcEvent"),
        ("IPO-MIB", "ipoGenAppOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenAppFailureSvcEvent"),
        ("IPO-MIB", "ipoGenAppSvcEvent"))
)
if mibBuilder.loadTexts:
    ipoGenSvcNotificationsGroup.setStatus(
        "current"
    )

ipoGenSvcSOGNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 8)
)
ipoGenSvcSOGNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenSogHostFailureSvcEvent"),
        ("IPO-MIB", "ipoGenSogModeChangeSvcEvent"))
)
if mibBuilder.loadTexts:
    ipoGenSvcSOGNotificationsGroup.setStatus(
        "current"
    )

ipoGenUPriLicSvcNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 9)
)
ipoGenUPriLicSvcNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenUPriLicChansReducedSvcEvent"),
        ("IPO-MIB", "ipoGenUPriLicCallRejectedSvcEvent"))
)
if mibBuilder.loadTexts:
    ipoGenUPriLicSvcNotificationsGroup.setStatus(
        "current"
    )

ipoGenSvcQoSMonNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 11)
)
ipoGenSvcQoSMonNotificationsGroup.setObjects(
    ("IPO-MIB", "ipoGenQoSMonSvcEvent")
)
if mibBuilder.loadTexts:
    ipoGenSvcQoSMonNotificationsGroup.setStatus(
        "current"
    )

ipoGenSvcSystemShutdownNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 13)
)
ipoGenSvcSystemShutdownNotificationsGroup.setObjects(
    ("IPO-MIB", "ipoGenSystemShutdownSvcEvent")
)
if mibBuilder.loadTexts:
    ipoGenSvcSystemShutdownNotificationsGroup.setStatus(
        "current"
    )

ipoGenSDcardNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 15)
)
ipoGenSDcardNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenAppOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenAppFailureSvcEvent"),
        ("IPO-MIB", "ipoGenAppSvcEvent"),
        ("IPO-MIB", "ipoGenSystemRunningBackupEvent"),
        ("IPO-MIB", "ipoGenInvalidMemoryCardEvent"),
        ("IPO-MIB", "ipoGenNoLicenceKeyDongleEvent"),
        ("IPO-MIB", "ipoGenMemoryCardCapacityEvent"))
)
if mibBuilder.loadTexts:
    ipoGenSDcardNotificationsGroup.setStatus(
        "current"
    )

ipoGenSvcMiscNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 2, 17)
)
ipoGenSvcMiscNotificationsGroup.setObjects(
      *(("IPO-MIB", "ipoGenConfigFailureSvcEvent"),
        ("IPO-MIB", "ipoGenConfigOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenConfigErrorSvcEvent"),
        ("IPO-MIB", "ipoGenConfigChangeSvcEvent"),
        ("IPO-MIB", "ipoGenServiceFailureSvcEvent"),
        ("IPO-MIB", "ipoGenServiceOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenServiceErrorSvcEvent"),
        ("IPO-MIB", "ipoGenServiceChangeSvcEvent"),
        ("IPO-MIB", "ipoGenTrunkFailureSvcEvent"),
        ("IPO-MIB", "ipoGenTrunkOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenTrunkErrorSvcEvent"),
        ("IPO-MIB", "ipoGenTrunkChangeSvcEvent"),
        ("IPO-MIB", "ipoGenLinkFailureSvcEvent"),
        ("IPO-MIB", "ipoGenLinkOperationalSvcEvent"),
        ("IPO-MIB", "ipoGenLinkErrorSvcEvent"),
        ("IPO-MIB", "ipoGenLinkChangeSvcEvent"),
        ("IPO-MIB", "ipoGenEmergencyCallSvcEvent"))
)
if mibBuilder.loadTexts:
    ipoGenSvcMiscNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipoGenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 1)
)
ipoGenCompliance.setObjects(
      *(("IPO-MIB", "ipoGenNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoGenCompliance.setStatus(
        "deprecated"
    )

ipoGen2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 2)
)
ipoGen2Compliance.setObjects(
      *(("IPO-MIB", "ipoGenNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen2Compliance.setStatus(
        "deprecated"
    )

ipoGen3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 3)
)
ipoGen3Compliance.setObjects(
      *(("IPO-MIB", "ipoGenv2NotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenEntGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcSOGNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen3Compliance.setStatus(
        "deprecated"
    )

ipoGen4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 4)
)
ipoGen4Compliance.setObjects(
      *(("IPO-MIB", "ipoGenv2NotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenEntGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcSOGNotificationsGroup"),
        ("IPO-MIB", "ipoGenUPriLicSvcNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen4Compliance.setStatus(
        "deprecated"
    )

ipoGen5Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 5)
)
ipoGen5Compliance.setObjects(
      *(("IPO-MIB", "ipoGenv2NotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenEntGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcSOGNotificationsGroup"),
        ("IPO-MIB", "ipoGenUPriLicSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenQosMonNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcQoSMonNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen5Compliance.setStatus(
        "deprecated"
    )

ipoGen6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 6)
)
ipoGen6Compliance.setObjects(
      *(("IPO-MIB", "ipoGenv2NotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenEntGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcSOGNotificationsGroup"),
        ("IPO-MIB", "ipoGenUPriLicSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcQoSMonNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcSystemShutdownNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcSystemShutdownObjectGroup"),
        ("IPO-MIB", "ipoGenSDcardNotificationsGroup"),
        ("IPO-MIB", "ipoGenSDcardNotificationObjectsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen6Compliance.setStatus(
        "deprecated"
    )

ipoGen7Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 3, 1, 7)
)
ipoGen7Compliance.setObjects(
      *(("IPO-MIB", "ipoGenv2NotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenEntGenNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcMiscNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcMiscNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSOGNotificationObjectsGroup"),
        ("IPO-MIB", "ipoGenSvcSOGNotificationsGroup"),
        ("IPO-MIB", "ipoGenUPriLicSvcNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcQoSMonNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcSystemShutdownNotificationsGroup"),
        ("IPO-MIB", "ipoGenSvcSystemShutdownObjectGroup"),
        ("IPO-MIB", "ipoGenSDcardNotificationsGroup"),
        ("IPO-MIB", "ipoGenSDcardNotificationObjectsGroup"))
)
if mibBuilder.loadTexts:
    ipoGen7Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPO-MIB",
    **{"ipoMIB": ipoMIB,
       "ipoGeneric": ipoGeneric,
       "ipoGenMibs": ipoGenMibs,
       "ipoGenTraps": ipoGenTraps,
       "ipoGTEvents": ipoGTEvents,
       "ipoGenEntityFailureEvent": ipoGenEntityFailureEvent,
       "ipoGenEntityOperationalEvent": ipoGenEntityOperationalEvent,
       "ipoGenEntityErrorEvent": ipoGenEntityErrorEvent,
       "ipoGenEntityChangeEvent": ipoGenEntityChangeEvent,
       "ipoGenLKSCommsFailureEvent": ipoGenLKSCommsFailureEvent,
       "ipoGenLKSCommsOperationalEvent": ipoGenLKSCommsOperationalEvent,
       "ipoGenLKSCommsErrorEvent": ipoGenLKSCommsErrorEvent,
       "ipoGenLKSCommsChangeEvent": ipoGenLKSCommsChangeEvent,
       "ipoGenLoopbackEvent": ipoGenLoopbackEvent,
       "ipoGenAppFailureEvent": ipoGenAppFailureEvent,
       "ipoGenAppOperationalEvent": ipoGenAppOperationalEvent,
       "ipoGenAppEvent": ipoGenAppEvent,
       "ipoGenSogHostFailureEvent": ipoGenSogHostFailureEvent,
       "ipoGenSogModeChangeEvent": ipoGenSogModeChangeEvent,
       "ipoGenColdStartSvcEvent": ipoGenColdStartSvcEvent,
       "ipoGenWarmStartSvcEvent": ipoGenWarmStartSvcEvent,
       "ipoGenLinkDownSvcEvent": ipoGenLinkDownSvcEvent,
       "ipoGenLinkUpSvcEvent": ipoGenLinkUpSvcEvent,
       "ipoGenAuthFailureSvcEvent": ipoGenAuthFailureSvcEvent,
       "ipoGenEntityFailureSvcEvent": ipoGenEntityFailureSvcEvent,
       "ipoGenEntityOperationalSvcEvent": ipoGenEntityOperationalSvcEvent,
       "ipoGenEntityErrorSvcEvent": ipoGenEntityErrorSvcEvent,
       "ipoGenEntityChangeSvcEvent": ipoGenEntityChangeSvcEvent,
       "ipoGenLKSCommsFailureSvcEvent": ipoGenLKSCommsFailureSvcEvent,
       "ipoGenLKSCommsOperationalSvcEvent": ipoGenLKSCommsOperationalSvcEvent,
       "ipoGenLKSCommsErrorSvcEvent": ipoGenLKSCommsErrorSvcEvent,
       "ipoGenLKSCommsChangeSvcEvent": ipoGenLKSCommsChangeSvcEvent,
       "ipoGenLoopbackSvcEvent": ipoGenLoopbackSvcEvent,
       "ipoGenAppFailureSvcEvent": ipoGenAppFailureSvcEvent,
       "ipoGenAppOperationalSvcEvent": ipoGenAppOperationalSvcEvent,
       "ipoGenAppSvcEvent": ipoGenAppSvcEvent,
       "ipoGenSogHostFailureSvcEvent": ipoGenSogHostFailureSvcEvent,
       "ipoGenSogModeChangeSvcEvent": ipoGenSogModeChangeSvcEvent,
       "ipoGenUPriLicChansReducedSvcEvent": ipoGenUPriLicChansReducedSvcEvent,
       "ipoGenUPriLicCallRejectedSvcEvent": ipoGenUPriLicCallRejectedSvcEvent,
       "ipoGenQoSMonSvcEvent": ipoGenQoSMonSvcEvent,
       "ipoGenSystemShutdownSvcEvent": ipoGenSystemShutdownSvcEvent,
       "ipoGenSystemRunningBackupEvent": ipoGenSystemRunningBackupEvent,
       "ipoGenInvalidMemoryCardEvent": ipoGenInvalidMemoryCardEvent,
       "ipoGenNoLicenceKeyDongleEvent": ipoGenNoLicenceKeyDongleEvent,
       "ipoGenMemoryCardCapacityEvent": ipoGenMemoryCardCapacityEvent,
       "ipoGenConfigFailureSvcEvent": ipoGenConfigFailureSvcEvent,
       "ipoGenConfigOperationalSvcEvent": ipoGenConfigOperationalSvcEvent,
       "ipoGenConfigErrorSvcEvent": ipoGenConfigErrorSvcEvent,
       "ipoGenConfigChangeSvcEvent": ipoGenConfigChangeSvcEvent,
       "ipoGenServiceFailureSvcEvent": ipoGenServiceFailureSvcEvent,
       "ipoGenServiceOperationalSvcEvent": ipoGenServiceOperationalSvcEvent,
       "ipoGenServiceErrorSvcEvent": ipoGenServiceErrorSvcEvent,
       "ipoGenServiceChangeSvcEvent": ipoGenServiceChangeSvcEvent,
       "ipoGenTrunkFailureSvcEvent": ipoGenTrunkFailureSvcEvent,
       "ipoGenTrunkOperationalSvcEvent": ipoGenTrunkOperationalSvcEvent,
       "ipoGenTrunkErrorSvcEvent": ipoGenTrunkErrorSvcEvent,
       "ipoGenTrunkChangeSvcEvent": ipoGenTrunkChangeSvcEvent,
       "ipoGenLinkFailureSvcEvent": ipoGenLinkFailureSvcEvent,
       "ipoGenLinkOperationalSvcEvent": ipoGenLinkOperationalSvcEvent,
       "ipoGenLinkErrorSvcEvent": ipoGenLinkErrorSvcEvent,
       "ipoGenLinkChangeSvcEvent": ipoGenLinkChangeSvcEvent,
       "ipoGenEmergencyCallSvcEvent": ipoGenEmergencyCallSvcEvent,
       "ipoGTObjects": ipoGTObjects,
       "ipoGTEventSeverity": ipoGTEventSeverity,
       "ipoGTEventDateTime": ipoGTEventDateTime,
       "ipoGTEventEntity": ipoGTEventEntity,
       "ipoGTEventLoopbackStatus": ipoGTEventLoopbackStatus,
       "ipoGTEventAppEntity": ipoGTEventAppEntity,
       "ipoGTEventAppEvent": ipoGTEventAppEvent,
       "ipoGTEventHostAddress": ipoGTEventHostAddress,
       "ipoGTEventSOGMode": ipoGTEventSOGMode,
       "ipoGTEventStdSeverity": ipoGTEventStdSeverity,
       "ipoGTEventDevID": ipoGTEventDevID,
       "ipoGTEventEntityName": ipoGTEventEntityName,
       "ipoGTEventLoopbackStatusBits": ipoGTEventLoopbackStatusBits,
       "ipoGTEventQoSMonJitter": ipoGTEventQoSMonJitter,
       "ipoGTEventQoSMonRndTrip": ipoGTEventQoSMonRndTrip,
       "ipoGTEventQoSMonPktLoss": ipoGTEventQoSMonPktLoss,
       "ipoGTEventQoSMonCallId": ipoGTEventQoSMonCallId,
       "ipoGTEventQoSMonDevType": ipoGTEventQoSMonDevType,
       "ipoGTEventQoSMonDevId": ipoGTEventQoSMonDevId,
       "ipoGTEventQoSMonExtnNo": ipoGTEventQoSMonExtnNo,
       "ipoGTEventSystemShutdownSource": ipoGTEventSystemShutdownSource,
       "ipoGTEventSystemShutdownTimeout": ipoGTEventSystemShutdownTimeout,
       "ipoGTEventMemoryCardSlotId": ipoGTEventMemoryCardSlotId,
       "ipoGTEventNoValidKeyReason": ipoGTEventNoValidKeyReason,
       "ipoGTEventReason": ipoGTEventReason,
       "ipoGTEventData": ipoGTEventData,
       "ipoGTEventAlarmDescription": ipoGTEventAlarmDescription,
       "ipoGTEventAlarmRemedialAction": ipoGTEventAlarmRemedialAction,
       "ipoGenConformance": ipoGenConformance,
       "ipoGenCompliances": ipoGenCompliances,
       "ipoGenCompliance": ipoGenCompliance,
       "ipoGen2Compliance": ipoGen2Compliance,
       "ipoGen3Compliance": ipoGen3Compliance,
       "ipoGen4Compliance": ipoGen4Compliance,
       "ipoGen5Compliance": ipoGen5Compliance,
       "ipoGen6Compliance": ipoGen6Compliance,
       "ipoGen7Compliance": ipoGen7Compliance,
       "ipoGenGroups": ipoGenGroups,
       "ipoGenNotificationObjectsGroup": ipoGenNotificationObjectsGroup,
       "ipoGenNotificationsGroup": ipoGenNotificationsGroup,
       "ipoGenSOGNotificationObjectsGroup": ipoGenSOGNotificationObjectsGroup,
       "ipoGenSOGNotificationsGroup": ipoGenSOGNotificationsGroup,
       "ipoGenv2NotificationObjectsGroup": ipoGenv2NotificationObjectsGroup,
       "ipoGenEntGenNotificationsGroup": ipoGenEntGenNotificationsGroup,
       "ipoGenSvcNotificationsGroup": ipoGenSvcNotificationsGroup,
       "ipoGenSvcSOGNotificationsGroup": ipoGenSvcSOGNotificationsGroup,
       "ipoGenUPriLicSvcNotificationsGroup": ipoGenUPriLicSvcNotificationsGroup,
       "ipoGenQosMonNotificationObjectsGroup": ipoGenQosMonNotificationObjectsGroup,
       "ipoGenSvcQoSMonNotificationsGroup": ipoGenSvcQoSMonNotificationsGroup,
       "ipoGenSvcSystemShutdownObjectGroup": ipoGenSvcSystemShutdownObjectGroup,
       "ipoGenSvcSystemShutdownNotificationsGroup": ipoGenSvcSystemShutdownNotificationsGroup,
       "ipoGenSDcardNotificationObjectsGroup": ipoGenSDcardNotificationObjectsGroup,
       "ipoGenSDcardNotificationsGroup": ipoGenSDcardNotificationsGroup,
       "ipoGenSvcMiscNotificationObjectsGroup": ipoGenSvcMiscNotificationObjectsGroup,
       "ipoGenSvcMiscNotificationsGroup": ipoGenSvcMiscNotificationsGroup}
)
