# SNMP MIB module (BCN-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-NTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:28 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

bcnNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bcnNtpMIB.setRevisions(
        ("2010-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NTPTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x.4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class NTPLeapIndicator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 0),
          ("addSecond", 1),
          ("subtractSecond", 2),
          ("alarm", 3))
    )



class NTPRefId(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_BcnNtp_ObjectIdentity = ObjectIdentity
bcnNtp = _BcnNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4)
)
_BcnNtpObjects_ObjectIdentity = ObjectIdentity
bcnNtpObjects = _BcnNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2)
)
_BcnNtpServiceStatus_ObjectIdentity = ObjectIdentity
bcnNtpServiceStatus = _BcnNtpServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    bcnNtpServiceStatus.setStatus("current")


class _BcnNtpSerOperState_Type(Integer32):
    """Custom type bcnNtpSerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2),
          ("starting", 3),
          ("stopping", 4),
          ("fault", 5))
    )


_BcnNtpSerOperState_Type.__name__ = "Integer32"
_BcnNtpSerOperState_Object = MibScalar
bcnNtpSerOperState = _BcnNtpSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1, 1),
    _BcnNtpSerOperState_Type()
)
bcnNtpSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSerOperState.setStatus("current")
_BcnNtpSystem_ObjectIdentity = ObjectIdentity
bcnNtpSystem = _BcnNtpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    bcnNtpSystem.setStatus("current")
_BcnNtpSysLeap_Type = NTPLeapIndicator
_BcnNtpSysLeap_Object = MibScalar
bcnNtpSysLeap = _BcnNtpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 1),
    _BcnNtpSysLeap_Type()
)
bcnNtpSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysLeap.setStatus("current")


class _BcnNtpSysStratum_Type(Integer32):
    """Custom type bcnNtpSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcnNtpSysStratum_Type.__name__ = "Integer32"
_BcnNtpSysStratum_Object = MibScalar
bcnNtpSysStratum = _BcnNtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 2),
    _BcnNtpSysStratum_Type()
)
bcnNtpSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysStratum.setStatus("current")
_BcnNtpSysPrecision_Type = Integer32
_BcnNtpSysPrecision_Object = MibScalar
bcnNtpSysPrecision = _BcnNtpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 3),
    _BcnNtpSysPrecision_Type()
)
bcnNtpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysPrecision.setStatus("current")
_BcnNtpSysRootDelay_Type = DisplayString
_BcnNtpSysRootDelay_Object = MibScalar
bcnNtpSysRootDelay = _BcnNtpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 4),
    _BcnNtpSysRootDelay_Type()
)
bcnNtpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysRootDelay.setStatus("current")
_BcnNtpSysRootDispersion_Type = DisplayString
_BcnNtpSysRootDispersion_Object = MibScalar
bcnNtpSysRootDispersion = _BcnNtpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 5),
    _BcnNtpSysRootDispersion_Type()
)
bcnNtpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysRootDispersion.setStatus("current")
_BcnNtpSysRefId_Type = NTPRefId
_BcnNtpSysRefId_Object = MibScalar
bcnNtpSysRefId = _BcnNtpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 6),
    _BcnNtpSysRefId_Type()
)
bcnNtpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysRefId.setStatus("current")
_BcnNtpSysRefTime_Type = NTPTimeStamp
_BcnNtpSysRefTime_Object = MibScalar
bcnNtpSysRefTime = _BcnNtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 7),
    _BcnNtpSysRefTime_Type()
)
bcnNtpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysRefTime.setStatus("current")
_BcnNtpSysPoll_Type = Integer32
_BcnNtpSysPoll_Object = MibScalar
bcnNtpSysPoll = _BcnNtpSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 8),
    _BcnNtpSysPoll_Type()
)
bcnNtpSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysPoll.setStatus("current")
_BcnNtpSysPeer_Type = Unsigned32
_BcnNtpSysPeer_Object = MibScalar
bcnNtpSysPeer = _BcnNtpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 9),
    _BcnNtpSysPeer_Type()
)
bcnNtpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysPeer.setStatus("current")
_BcnNtpSysFreq_Type = DisplayString
_BcnNtpSysFreq_Object = MibScalar
bcnNtpSysFreq = _BcnNtpSysFreq_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 10),
    _BcnNtpSysFreq_Type()
)
bcnNtpSysFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysFreq.setStatus("current")
_BcnNtpSysClock_Type = NTPTimeStamp
_BcnNtpSysClock_Object = MibScalar
bcnNtpSysClock = _BcnNtpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 11),
    _BcnNtpSysClock_Type()
)
bcnNtpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysClock.setStatus("current")
_BcnNtpSysSystem_Type = DisplayString
_BcnNtpSysSystem_Object = MibScalar
bcnNtpSysSystem = _BcnNtpSysSystem_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 12),
    _BcnNtpSysSystem_Type()
)
bcnNtpSysSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysSystem.setStatus("current")
_BcnNtpSysProcessor_Type = DisplayString
_BcnNtpSysProcessor_Object = MibScalar
bcnNtpSysProcessor = _BcnNtpSysProcessor_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 13),
    _BcnNtpSysProcessor_Type()
)
bcnNtpSysProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysProcessor.setStatus("current")
_BcnNtpSysJitter_Type = DisplayString
_BcnNtpSysJitter_Object = MibScalar
bcnNtpSysJitter = _BcnNtpSysJitter_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 14),
    _BcnNtpSysJitter_Type()
)
bcnNtpSysJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpSysJitter.setStatus("current")
_BcnNtpPeers_ObjectIdentity = ObjectIdentity
bcnNtpPeers = _BcnNtpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    bcnNtpPeers.setStatus("current")
_BcnNtpPeersVarTable_Object = MibTable
bcnNtpPeersVarTable = _BcnNtpPeersVarTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    bcnNtpPeersVarTable.setStatus("current")
_BcnNtpPeersVarEntry_Object = MibTableRow
bcnNtpPeersVarEntry = _BcnNtpPeersVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1)
)
bcnNtpPeersVarEntry.setIndexNames(
    (0, "BCN-NTP-MIB", "bcnNtpPeersAssocId"),
)
if mibBuilder.loadTexts:
    bcnNtpPeersVarEntry.setStatus("current")
_BcnNtpPeersAssocId_Type = Unsigned32
_BcnNtpPeersAssocId_Object = MibTableColumn
bcnNtpPeersAssocId = _BcnNtpPeersAssocId_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 1),
    _BcnNtpPeersAssocId_Type()
)
bcnNtpPeersAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnNtpPeersAssocId.setStatus("current")
_BcnNtpPeersConfigured_Type = TruthValue
_BcnNtpPeersConfigured_Object = MibTableColumn
bcnNtpPeersConfigured = _BcnNtpPeersConfigured_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 2),
    _BcnNtpPeersConfigured_Type()
)
bcnNtpPeersConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersConfigured.setStatus("current")
_BcnNtpPeersPeerAddressType_Type = InetAddressType
_BcnNtpPeersPeerAddressType_Object = MibTableColumn
bcnNtpPeersPeerAddressType = _BcnNtpPeersPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 3),
    _BcnNtpPeersPeerAddressType_Type()
)
bcnNtpPeersPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersPeerAddressType.setStatus("current")
_BcnNtpPeersPeerAddress_Type = InetAddress
_BcnNtpPeersPeerAddress_Object = MibTableColumn
bcnNtpPeersPeerAddress = _BcnNtpPeersPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 4),
    _BcnNtpPeersPeerAddress_Type()
)
bcnNtpPeersPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersPeerAddress.setStatus("current")
_BcnNtpPeersPeerPort_Type = InetPortNumber
_BcnNtpPeersPeerPort_Object = MibTableColumn
bcnNtpPeersPeerPort = _BcnNtpPeersPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 5),
    _BcnNtpPeersPeerPort_Type()
)
bcnNtpPeersPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersPeerPort.setStatus("current")
_BcnNtpPeersHostAddressType_Type = InetAddressType
_BcnNtpPeersHostAddressType_Object = MibTableColumn
bcnNtpPeersHostAddressType = _BcnNtpPeersHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 6),
    _BcnNtpPeersHostAddressType_Type()
)
bcnNtpPeersHostAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersHostAddressType.setStatus("current")
_BcnNtpPeersHostAddress_Type = InetAddress
_BcnNtpPeersHostAddress_Object = MibTableColumn
bcnNtpPeersHostAddress = _BcnNtpPeersHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 7),
    _BcnNtpPeersHostAddress_Type()
)
bcnNtpPeersHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersHostAddress.setStatus("current")
_BcnNtpPeersHostPort_Type = InetPortNumber
_BcnNtpPeersHostPort_Object = MibTableColumn
bcnNtpPeersHostPort = _BcnNtpPeersHostPort_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 8),
    _BcnNtpPeersHostPort_Type()
)
bcnNtpPeersHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersHostPort.setStatus("current")
_BcnNtpPeersLeap_Type = NTPLeapIndicator
_BcnNtpPeersLeap_Object = MibTableColumn
bcnNtpPeersLeap = _BcnNtpPeersLeap_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 9),
    _BcnNtpPeersLeap_Type()
)
bcnNtpPeersLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersLeap.setStatus("current")


class _BcnNtpPeersMode_Type(Integer32):
    """Custom type bcnNtpPeersMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5),
          ("reservedControl", 6),
          ("reservedPrivate", 7))
    )


_BcnNtpPeersMode_Type.__name__ = "Integer32"
_BcnNtpPeersMode_Object = MibTableColumn
bcnNtpPeersMode = _BcnNtpPeersMode_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 10),
    _BcnNtpPeersMode_Type()
)
bcnNtpPeersMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersMode.setStatus("current")


class _BcnNtpPeersStratum_Type(Integer32):
    """Custom type bcnNtpPeersStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcnNtpPeersStratum_Type.__name__ = "Integer32"
_BcnNtpPeersStratum_Object = MibTableColumn
bcnNtpPeersStratum = _BcnNtpPeersStratum_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 11),
    _BcnNtpPeersStratum_Type()
)
bcnNtpPeersStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersStratum.setStatus("current")
_BcnNtpPeersPeerPoll_Type = Integer32
_BcnNtpPeersPeerPoll_Object = MibTableColumn
bcnNtpPeersPeerPoll = _BcnNtpPeersPeerPoll_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 12),
    _BcnNtpPeersPeerPoll_Type()
)
bcnNtpPeersPeerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersPeerPoll.setStatus("current")
_BcnNtpPeersHostPoll_Type = Integer32
_BcnNtpPeersHostPoll_Object = MibTableColumn
bcnNtpPeersHostPoll = _BcnNtpPeersHostPoll_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 13),
    _BcnNtpPeersHostPoll_Type()
)
bcnNtpPeersHostPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersHostPoll.setStatus("current")
_BcnNtpPeersPrecision_Type = Integer32
_BcnNtpPeersPrecision_Object = MibTableColumn
bcnNtpPeersPrecision = _BcnNtpPeersPrecision_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 14),
    _BcnNtpPeersPrecision_Type()
)
bcnNtpPeersPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersPrecision.setStatus("current")
_BcnNtpPeersRootDelay_Type = DisplayString
_BcnNtpPeersRootDelay_Object = MibTableColumn
bcnNtpPeersRootDelay = _BcnNtpPeersRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 15),
    _BcnNtpPeersRootDelay_Type()
)
bcnNtpPeersRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersRootDelay.setStatus("current")
_BcnNtpPeersRootDispersion_Type = DisplayString
_BcnNtpPeersRootDispersion_Object = MibTableColumn
bcnNtpPeersRootDispersion = _BcnNtpPeersRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 16),
    _BcnNtpPeersRootDispersion_Type()
)
bcnNtpPeersRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersRootDispersion.setStatus("current")
_BcnNtpPeersRefId_Type = NTPRefId
_BcnNtpPeersRefId_Object = MibTableColumn
bcnNtpPeersRefId = _BcnNtpPeersRefId_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 17),
    _BcnNtpPeersRefId_Type()
)
bcnNtpPeersRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersRefId.setStatus("current")
_BcnNtpPeersRefTime_Type = NTPTimeStamp
_BcnNtpPeersRefTime_Object = MibTableColumn
bcnNtpPeersRefTime = _BcnNtpPeersRefTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 18),
    _BcnNtpPeersRefTime_Type()
)
bcnNtpPeersRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersRefTime.setStatus("current")
_BcnNtpPeersOrgTime_Type = NTPTimeStamp
_BcnNtpPeersOrgTime_Object = MibTableColumn
bcnNtpPeersOrgTime = _BcnNtpPeersOrgTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 19),
    _BcnNtpPeersOrgTime_Type()
)
bcnNtpPeersOrgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersOrgTime.setStatus("current")
_BcnNtpPeersReceiveTime_Type = NTPTimeStamp
_BcnNtpPeersReceiveTime_Object = MibTableColumn
bcnNtpPeersReceiveTime = _BcnNtpPeersReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 20),
    _BcnNtpPeersReceiveTime_Type()
)
bcnNtpPeersReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersReceiveTime.setStatus("current")
_BcnNtpPeersTransmitTime_Type = NTPTimeStamp
_BcnNtpPeersTransmitTime_Object = MibTableColumn
bcnNtpPeersTransmitTime = _BcnNtpPeersTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 21),
    _BcnNtpPeersTransmitTime_Type()
)
bcnNtpPeersTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersTransmitTime.setStatus("current")
_BcnNtpPeersReach_Type = Unsigned32
_BcnNtpPeersReach_Object = MibTableColumn
bcnNtpPeersReach = _BcnNtpPeersReach_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 22),
    _BcnNtpPeersReach_Type()
)
bcnNtpPeersReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersReach.setStatus("current")
_BcnNtpPeersOffset_Type = DisplayString
_BcnNtpPeersOffset_Object = MibTableColumn
bcnNtpPeersOffset = _BcnNtpPeersOffset_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 23),
    _BcnNtpPeersOffset_Type()
)
bcnNtpPeersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersOffset.setStatus("current")
_BcnNtpPeersDelay_Type = DisplayString
_BcnNtpPeersDelay_Object = MibTableColumn
bcnNtpPeersDelay = _BcnNtpPeersDelay_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 24),
    _BcnNtpPeersDelay_Type()
)
bcnNtpPeersDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersDelay.setStatus("current")
_BcnNtpPeersDispersion_Type = DisplayString
_BcnNtpPeersDispersion_Object = MibTableColumn
bcnNtpPeersDispersion = _BcnNtpPeersDispersion_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 25),
    _BcnNtpPeersDispersion_Type()
)
bcnNtpPeersDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersDispersion.setStatus("current")
_BcnNtpPeersJitter_Type = DisplayString
_BcnNtpPeersJitter_Object = MibTableColumn
bcnNtpPeersJitter = _BcnNtpPeersJitter_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 26),
    _BcnNtpPeersJitter_Type()
)
bcnNtpPeersJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnNtpPeersJitter.setStatus("current")
_BcnNtpNotification_ObjectIdentity = ObjectIdentity
bcnNtpNotification = _BcnNtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3)
)
_BcnNtpNotificationEvents_ObjectIdentity = ObjectIdentity
bcnNtpNotificationEvents = _BcnNtpNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0)
)
_BcnNtpNotificationData_ObjectIdentity = ObjectIdentity
bcnNtpNotificationData = _BcnNtpNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1)
)
_BcnNtpAlarmSeverity_Type = BcnAlarmSeverity
_BcnNtpAlarmSeverity_Object = MibScalar
bcnNtpAlarmSeverity = _BcnNtpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 1),
    _BcnNtpAlarmSeverity_Type()
)
bcnNtpAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnNtpAlarmSeverity.setStatus("current")
_BcnNtpAlarmInfo_Type = DisplayString
_BcnNtpAlarmInfo_Object = MibScalar
bcnNtpAlarmInfo = _BcnNtpAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 2),
    _BcnNtpAlarmInfo_Type()
)
bcnNtpAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnNtpAlarmInfo.setStatus("current")
_BcnNtpConformance_ObjectIdentity = ObjectIdentity
bcnNtpConformance = _BcnNtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4)
)
_BcnNtpServiceCompliances_ObjectIdentity = ObjectIdentity
bcnNtpServiceCompliances = _BcnNtpServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1)
)
_BcnNtpServiceGroups_ObjectIdentity = ObjectIdentity
bcnNtpServiceGroups = _BcnNtpServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2)
)

# Managed Objects groups

bcnNtpServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 1)
)
bcnNtpServiceStatusGroup.setObjects(
    ("BCN-NTP-MIB", "bcnNtpSerOperState")
)
if mibBuilder.loadTexts:
    bcnNtpServiceStatusGroup.setStatus("current")

bcnNtpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 2)
)
bcnNtpSystemGroup.setObjects(
      *(("BCN-NTP-MIB", "bcnNtpSysLeap"),
        ("BCN-NTP-MIB", "bcnNtpSysStratum"),
        ("BCN-NTP-MIB", "bcnNtpSysPrecision"),
        ("BCN-NTP-MIB", "bcnNtpSysRootDelay"),
        ("BCN-NTP-MIB", "bcnNtpSysRootDispersion"),
        ("BCN-NTP-MIB", "bcnNtpSysRefId"),
        ("BCN-NTP-MIB", "bcnNtpSysRefTime"),
        ("BCN-NTP-MIB", "bcnNtpSysPoll"),
        ("BCN-NTP-MIB", "bcnNtpSysPeer"),
        ("BCN-NTP-MIB", "bcnNtpSysFreq"),
        ("BCN-NTP-MIB", "bcnNtpSysClock"),
        ("BCN-NTP-MIB", "bcnNtpSysSystem"),
        ("BCN-NTP-MIB", "bcnNtpSysProcessor"),
        ("BCN-NTP-MIB", "bcnNtpSysJitter"))
)
if mibBuilder.loadTexts:
    bcnNtpSystemGroup.setStatus("current")

bcnNtpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 3)
)
bcnNtpPeersGroup.setObjects(
      *(("BCN-NTP-MIB", "bcnNtpPeersConfigured"),
        ("BCN-NTP-MIB", "bcnNtpPeersPeerAddressType"),
        ("BCN-NTP-MIB", "bcnNtpPeersPeerAddress"),
        ("BCN-NTP-MIB", "bcnNtpPeersPeerPort"),
        ("BCN-NTP-MIB", "bcnNtpPeersHostAddressType"),
        ("BCN-NTP-MIB", "bcnNtpPeersHostAddress"),
        ("BCN-NTP-MIB", "bcnNtpPeersHostPort"),
        ("BCN-NTP-MIB", "bcnNtpPeersLeap"),
        ("BCN-NTP-MIB", "bcnNtpPeersMode"),
        ("BCN-NTP-MIB", "bcnNtpPeersStratum"),
        ("BCN-NTP-MIB", "bcnNtpPeersPeerPoll"),
        ("BCN-NTP-MIB", "bcnNtpPeersHostPoll"),
        ("BCN-NTP-MIB", "bcnNtpPeersPrecision"),
        ("BCN-NTP-MIB", "bcnNtpPeersRootDelay"),
        ("BCN-NTP-MIB", "bcnNtpPeersRootDispersion"),
        ("BCN-NTP-MIB", "bcnNtpPeersRefId"),
        ("BCN-NTP-MIB", "bcnNtpPeersRefTime"),
        ("BCN-NTP-MIB", "bcnNtpPeersOrgTime"),
        ("BCN-NTP-MIB", "bcnNtpPeersReceiveTime"),
        ("BCN-NTP-MIB", "bcnNtpPeersTransmitTime"),
        ("BCN-NTP-MIB", "bcnNtpPeersReach"),
        ("BCN-NTP-MIB", "bcnNtpPeersOffset"),
        ("BCN-NTP-MIB", "bcnNtpPeersDelay"),
        ("BCN-NTP-MIB", "bcnNtpPeersDispersion"),
        ("BCN-NTP-MIB", "bcnNtpPeersJitter"))
)
if mibBuilder.loadTexts:
    bcnNtpPeersGroup.setStatus("current")

bcnNtpNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 5)
)
bcnNtpNotificationDataGroup.setObjects(
      *(("BCN-NTP-MIB", "bcnNtpAlarmSeverity"),
        ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnNtpNotificationDataGroup.setStatus("current")


# Notification objects

bcnNtpAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0, 1)
)
bcnNtpAlarmNotif.setObjects(
      *(("BCN-NTP-MIB", "bcnNtpSerOperState"),
        ("BCN-NTP-MIB", "bcnNtpAlarmSeverity"),
        ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnNtpAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnNtpNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 4)
)
bcnNtpNotificationEventGroup.setObjects(
    ("BCN-NTP-MIB", "bcnNtpAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnNtpNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnNtpStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1, 1)
)
bcnNtpStatusCompliance.setObjects(
      *(("BCN-NTP-MIB", "bcnNtpServiceStatusGroup"),
        ("BCN-NTP-MIB", "bcnNtpSystemGroup"),
        ("BCN-NTP-MIB", "bcnNtpPeersGroup"),
        ("BCN-NTP-MIB", "bcnNtpNotificationEventGroup"),
        ("BCN-NTP-MIB", "bcnNtpNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnNtpStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPRefId": NTPRefId,
       "bcnNtp": bcnNtp,
       "bcnNtpMIB": bcnNtpMIB,
       "bcnNtpObjects": bcnNtpObjects,
       "bcnNtpServiceStatus": bcnNtpServiceStatus,
       "bcnNtpSerOperState": bcnNtpSerOperState,
       "bcnNtpSystem": bcnNtpSystem,
       "bcnNtpSysLeap": bcnNtpSysLeap,
       "bcnNtpSysStratum": bcnNtpSysStratum,
       "bcnNtpSysPrecision": bcnNtpSysPrecision,
       "bcnNtpSysRootDelay": bcnNtpSysRootDelay,
       "bcnNtpSysRootDispersion": bcnNtpSysRootDispersion,
       "bcnNtpSysRefId": bcnNtpSysRefId,
       "bcnNtpSysRefTime": bcnNtpSysRefTime,
       "bcnNtpSysPoll": bcnNtpSysPoll,
       "bcnNtpSysPeer": bcnNtpSysPeer,
       "bcnNtpSysFreq": bcnNtpSysFreq,
       "bcnNtpSysClock": bcnNtpSysClock,
       "bcnNtpSysSystem": bcnNtpSysSystem,
       "bcnNtpSysProcessor": bcnNtpSysProcessor,
       "bcnNtpSysJitter": bcnNtpSysJitter,
       "bcnNtpPeers": bcnNtpPeers,
       "bcnNtpPeersVarTable": bcnNtpPeersVarTable,
       "bcnNtpPeersVarEntry": bcnNtpPeersVarEntry,
       "bcnNtpPeersAssocId": bcnNtpPeersAssocId,
       "bcnNtpPeersConfigured": bcnNtpPeersConfigured,
       "bcnNtpPeersPeerAddressType": bcnNtpPeersPeerAddressType,
       "bcnNtpPeersPeerAddress": bcnNtpPeersPeerAddress,
       "bcnNtpPeersPeerPort": bcnNtpPeersPeerPort,
       "bcnNtpPeersHostAddressType": bcnNtpPeersHostAddressType,
       "bcnNtpPeersHostAddress": bcnNtpPeersHostAddress,
       "bcnNtpPeersHostPort": bcnNtpPeersHostPort,
       "bcnNtpPeersLeap": bcnNtpPeersLeap,
       "bcnNtpPeersMode": bcnNtpPeersMode,
       "bcnNtpPeersStratum": bcnNtpPeersStratum,
       "bcnNtpPeersPeerPoll": bcnNtpPeersPeerPoll,
       "bcnNtpPeersHostPoll": bcnNtpPeersHostPoll,
       "bcnNtpPeersPrecision": bcnNtpPeersPrecision,
       "bcnNtpPeersRootDelay": bcnNtpPeersRootDelay,
       "bcnNtpPeersRootDispersion": bcnNtpPeersRootDispersion,
       "bcnNtpPeersRefId": bcnNtpPeersRefId,
       "bcnNtpPeersRefTime": bcnNtpPeersRefTime,
       "bcnNtpPeersOrgTime": bcnNtpPeersOrgTime,
       "bcnNtpPeersReceiveTime": bcnNtpPeersReceiveTime,
       "bcnNtpPeersTransmitTime": bcnNtpPeersTransmitTime,
       "bcnNtpPeersReach": bcnNtpPeersReach,
       "bcnNtpPeersOffset": bcnNtpPeersOffset,
       "bcnNtpPeersDelay": bcnNtpPeersDelay,
       "bcnNtpPeersDispersion": bcnNtpPeersDispersion,
       "bcnNtpPeersJitter": bcnNtpPeersJitter,
       "bcnNtpNotification": bcnNtpNotification,
       "bcnNtpNotificationEvents": bcnNtpNotificationEvents,
       "bcnNtpAlarmNotif": bcnNtpAlarmNotif,
       "bcnNtpNotificationData": bcnNtpNotificationData,
       "bcnNtpAlarmSeverity": bcnNtpAlarmSeverity,
       "bcnNtpAlarmInfo": bcnNtpAlarmInfo,
       "bcnNtpConformance": bcnNtpConformance,
       "bcnNtpServiceCompliances": bcnNtpServiceCompliances,
       "bcnNtpStatusCompliance": bcnNtpStatusCompliance,
       "bcnNtpServiceGroups": bcnNtpServiceGroups,
       "bcnNtpServiceStatusGroup": bcnNtpServiceStatusGroup,
       "bcnNtpSystemGroup": bcnNtpSystemGroup,
       "bcnNtpPeersGroup": bcnNtpPeersGroup,
       "bcnNtpNotificationEventGroup": bcnNtpNotificationEventGroup,
       "bcnNtpNotificationDataGroup": bcnNtpNotificationDataGroup}
)
