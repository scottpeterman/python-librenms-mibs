# SNMP MIB module (PAN-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\paloaltonetworks\PAN-TRAPS
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:21 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(panCommonEventEventsV2,
 panCommonEventObjs) = mibBuilder.importSymbols(
    "PAN-COMMON-MIB",
    "panCommonEventEventsV2",
    "panCommonEventObjs")

(panCommonMib,
 panModules) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panCommonMib",
    "panModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

panTrapMibsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 5)
)
if mibBuilder.loadTexts:
    panTrapMibsModule.setRevisions(
        ("2018-05-01 00:00",
         "2018-01-01 00:00",
         "2017-11-28 00:00",
         "2017-10-01 00:00",
         "2016-06-28 00:00",
         "2016-01-25 00:00",
         "2015-09-30 00:00",
         "2015-02-26 00:00",
         "2014-07-09 00:00",
         "2011-06-27 10:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PanReceiveTime_Type(OctetString):
    """Custom type panReceiveTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanReceiveTime_Type.__name__ = "OctetString"
_PanReceiveTime_Object = MibScalar
panReceiveTime = _PanReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 2),
    _PanReceiveTime_Type()
)
panReceiveTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReceiveTime.setStatus("current")


class _PanSerial_Type(OctetString):
    """Custom type panSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSerial_Type.__name__ = "OctetString"
_PanSerial_Object = MibScalar
panSerial = _PanSerial_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 3),
    _PanSerial_Type()
)
panSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSerial.setStatus("current")


class _PanEventType_Type(OctetString):
    """Custom type panEventType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanEventType_Type.__name__ = "OctetString"
_PanEventType_Object = MibScalar
panEventType = _PanEventType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 4),
    _PanEventType_Type()
)
panEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEventType.setStatus("current")


class _PanEventSubType_Type(OctetString):
    """Custom type panEventSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanEventSubType_Type.__name__ = "OctetString"
_PanEventSubType_Object = MibScalar
panEventSubType = _PanEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 5),
    _PanEventSubType_Type()
)
panEventSubType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEventSubType.setStatus("current")
_PanHost_Type = IpAddress
_PanHost_Object = MibScalar
panHost = _PanHost_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 6),
    _PanHost_Type()
)
panHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHost.setStatus("current")


class _PanVsys_Type(OctetString):
    """Custom type panVsys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanVsys_Type.__name__ = "OctetString"
_PanVsys_Object = MibScalar
panVsys = _PanVsys_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 7),
    _PanVsys_Type()
)
panVsys.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panVsys.setStatus("current")
_PanSeqno_Type = Counter64
_PanSeqno_Object = MibScalar
panSeqno = _PanSeqno_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 8),
    _PanSeqno_Type()
)
panSeqno.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSeqno.setStatus("current")


class _PanActionflags_Type(OctetString):
    """Custom type panActionflags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanActionflags_Type.__name__ = "OctetString"
_PanActionflags_Object = MibScalar
panActionflags = _PanActionflags_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 9),
    _PanActionflags_Type()
)
panActionflags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panActionflags.setStatus("current")
_PanHostInetAddrType_Type = InetAddressType
_PanHostInetAddrType_Object = MibScalar
panHostInetAddrType = _PanHostInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 10),
    _PanHostInetAddrType_Type()
)
panHostInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHostInetAddrType.setStatus("current")
_PanHostInetAddr_Type = InetAddress
_PanHostInetAddr_Object = MibScalar
panHostInetAddr = _PanHostInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 11),
    _PanHostInetAddr_Type()
)
panHostInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHostInetAddr.setStatus("current")


class _PanHostname_Type(OctetString):
    """Custom type panHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHostname_Type.__name__ = "OctetString"
_PanHostname_Object = MibScalar
panHostname = _PanHostname_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 12),
    _PanHostname_Type()
)
panHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHostname.setStatus("current")
_PanSource_Type = IpAddress
_PanSource_Object = MibScalar
panSource = _PanSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 50),
    _PanSource_Type()
)
panSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSource.setStatus("current")
_PanDestination_Type = IpAddress
_PanDestination_Object = MibScalar
panDestination = _PanDestination_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 51),
    _PanDestination_Type()
)
panDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestination.setStatus("current")
_PanNatSource_Type = IpAddress
_PanNatSource_Object = MibScalar
panNatSource = _PanNatSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 52),
    _PanNatSource_Type()
)
panNatSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSource.setStatus("current")
_PanNatDestination_Type = IpAddress
_PanNatDestination_Object = MibScalar
panNatDestination = _PanNatDestination_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 53),
    _PanNatDestination_Type()
)
panNatDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestination.setStatus("current")


class _PanRule_Type(OctetString):
    """Custom type panRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanRule_Type.__name__ = "OctetString"
_PanRule_Object = MibScalar
panRule = _PanRule_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 54),
    _PanRule_Type()
)
panRule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRule.setStatus("current")


class _PanSrcUser_Type(OctetString):
    """Custom type panSrcUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSrcUser_Type.__name__ = "OctetString"
_PanSrcUser_Object = MibScalar
panSrcUser = _PanSrcUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 55),
    _PanSrcUser_Type()
)
panSrcUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSrcUser.setStatus("current")


class _PanDstUser_Type(OctetString):
    """Custom type panDstUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanDstUser_Type.__name__ = "OctetString"
_PanDstUser_Object = MibScalar
panDstUser = _PanDstUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 56),
    _PanDstUser_Type()
)
panDstUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDstUser.setStatus("current")


class _PanApplication_Type(OctetString):
    """Custom type panApplication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanApplication_Type.__name__ = "OctetString"
_PanApplication_Object = MibScalar
panApplication = _PanApplication_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 57),
    _PanApplication_Type()
)
panApplication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panApplication.setStatus("current")


class _PanSourceZone_Type(OctetString):
    """Custom type panSourceZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSourceZone_Type.__name__ = "OctetString"
_PanSourceZone_Object = MibScalar
panSourceZone = _PanSourceZone_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 58),
    _PanSourceZone_Type()
)
panSourceZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceZone.setStatus("current")


class _PanDestinationZone_Type(OctetString):
    """Custom type panDestinationZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanDestinationZone_Type.__name__ = "OctetString"
_PanDestinationZone_Object = MibScalar
panDestinationZone = _PanDestinationZone_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 59),
    _PanDestinationZone_Type()
)
panDestinationZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationZone.setStatus("current")


class _PanIngressInterface_Type(OctetString):
    """Custom type panIngressInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanIngressInterface_Type.__name__ = "OctetString"
_PanIngressInterface_Object = MibScalar
panIngressInterface = _PanIngressInterface_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 60),
    _PanIngressInterface_Type()
)
panIngressInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIngressInterface.setStatus("current")


class _PanEgressInterface_Type(OctetString):
    """Custom type panEgressInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanEgressInterface_Type.__name__ = "OctetString"
_PanEgressInterface_Object = MibScalar
panEgressInterface = _PanEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 61),
    _PanEgressInterface_Type()
)
panEgressInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEgressInterface.setStatus("current")


class _PanLogForwardingProfile_Type(OctetString):
    """Custom type panLogForwardingProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanLogForwardingProfile_Type.__name__ = "OctetString"
_PanLogForwardingProfile_Object = MibScalar
panLogForwardingProfile = _PanLogForwardingProfile_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 62),
    _PanLogForwardingProfile_Type()
)
panLogForwardingProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panLogForwardingProfile.setStatus("current")
_PanSessionID_Type = Counter32
_PanSessionID_Object = MibScalar
panSessionID = _PanSessionID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 63),
    _PanSessionID_Type()
)
panSessionID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSessionID.setStatus("current")
_PanRepeatCount_Type = Counter32
_PanRepeatCount_Object = MibScalar
panRepeatCount = _PanRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 64),
    _PanRepeatCount_Type()
)
panRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRepeatCount.setStatus("current")
_PanSourcePort_Type = Counter32
_PanSourcePort_Object = MibScalar
panSourcePort = _PanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 65),
    _PanSourcePort_Type()
)
panSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourcePort.setStatus("current")
_PanDestinationPort_Type = Counter32
_PanDestinationPort_Object = MibScalar
panDestinationPort = _PanDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 66),
    _PanDestinationPort_Type()
)
panDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationPort.setStatus("current")
_PanNatSourcePort_Type = Counter32
_PanNatSourcePort_Object = MibScalar
panNatSourcePort = _PanNatSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 67),
    _PanNatSourcePort_Type()
)
panNatSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourcePort.setStatus("current")
_PanNatDestinationPort_Type = Counter32
_PanNatDestinationPort_Object = MibScalar
panNatDestinationPort = _PanNatDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 68),
    _PanNatDestinationPort_Type()
)
panNatDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationPort.setStatus("current")


class _PanFlags_Type(OctetString):
    """Custom type panFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanFlags_Type.__name__ = "OctetString"
_PanFlags_Object = MibScalar
panFlags = _PanFlags_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 69),
    _PanFlags_Type()
)
panFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFlags.setStatus("current")


class _PanProtocol_Type(OctetString):
    """Custom type panProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanProtocol_Type.__name__ = "OctetString"
_PanProtocol_Object = MibScalar
panProtocol = _PanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 70),
    _PanProtocol_Type()
)
panProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panProtocol.setStatus("current")


class _PanAction_Type(OctetString):
    """Custom type panAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAction_Type.__name__ = "OctetString"
_PanAction_Object = MibScalar
panAction = _PanAction_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 71),
    _PanAction_Type()
)
panAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAction.setStatus("current")


class _PanTimeGenerated_Type(OctetString):
    """Custom type panTimeGenerated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTimeGenerated_Type.__name__ = "OctetString"
_PanTimeGenerated_Object = MibScalar
panTimeGenerated = _PanTimeGenerated_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 72),
    _PanTimeGenerated_Type()
)
panTimeGenerated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTimeGenerated.setStatus("current")


class _PanSrcloc_Type(OctetString):
    """Custom type panSrcloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSrcloc_Type.__name__ = "OctetString"
_PanSrcloc_Object = MibScalar
panSrcloc = _PanSrcloc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 73),
    _PanSrcloc_Type()
)
panSrcloc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSrcloc.setStatus("current")


class _PanDstloc_Type(OctetString):
    """Custom type panDstloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanDstloc_Type.__name__ = "OctetString"
_PanDstloc_Object = MibScalar
panDstloc = _PanDstloc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 74),
    _PanDstloc_Type()
)
panDstloc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDstloc.setStatus("current")
_PanSourceInetAddrType_Type = InetAddressType
_PanSourceInetAddrType_Object = MibScalar
panSourceInetAddrType = _PanSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 75),
    _PanSourceInetAddrType_Type()
)
panSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceInetAddrType.setStatus("current")
_PanSourceInetAddr_Type = InetAddress
_PanSourceInetAddr_Object = MibScalar
panSourceInetAddr = _PanSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 76),
    _PanSourceInetAddr_Type()
)
panSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceInetAddr.setStatus("current")
_PanDestinationInetAddrType_Type = InetAddressType
_PanDestinationInetAddrType_Object = MibScalar
panDestinationInetAddrType = _PanDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 77),
    _PanDestinationInetAddrType_Type()
)
panDestinationInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationInetAddrType.setStatus("current")
_PanDestinationInetAddr_Type = InetAddress
_PanDestinationInetAddr_Object = MibScalar
panDestinationInetAddr = _PanDestinationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 78),
    _PanDestinationInetAddr_Type()
)
panDestinationInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationInetAddr.setStatus("current")
_PanNatSourceInetAddrType_Type = InetAddressType
_PanNatSourceInetAddrType_Object = MibScalar
panNatSourceInetAddrType = _PanNatSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 79),
    _PanNatSourceInetAddrType_Type()
)
panNatSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourceInetAddrType.setStatus("current")
_PanNatSourceInetAddr_Type = InetAddress
_PanNatSourceInetAddr_Object = MibScalar
panNatSourceInetAddr = _PanNatSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 80),
    _PanNatSourceInetAddr_Type()
)
panNatSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourceInetAddr.setStatus("current")
_PanNatDestinationInetAddrType_Type = InetAddressType
_PanNatDestinationInetAddrType_Object = MibScalar
panNatDestinationInetAddrType = _PanNatDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 81),
    _PanNatDestinationInetAddrType_Type()
)
panNatDestinationInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationInetAddrType.setStatus("current")
_PanNatDestinationInetAddr_Type = InetAddress
_PanNatDestinationInetAddr_Object = MibScalar
panNatDestinationInetAddr = _PanNatDestinationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 82),
    _PanNatDestinationInetAddr_Type()
)
panNatDestinationInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationInetAddr.setStatus("current")


class _PanSourceUUID_Type(OctetString):
    """Custom type panSourceUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_PanSourceUUID_Type.__name__ = "OctetString"
_PanSourceUUID_Object = MibScalar
panSourceUUID = _PanSourceUUID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 83),
    _PanSourceUUID_Type()
)
panSourceUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceUUID.setStatus("current")


class _PanDestinationUUID_Type(OctetString):
    """Custom type panDestinationUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_PanDestinationUUID_Type.__name__ = "OctetString"
_PanDestinationUUID_Object = MibScalar
panDestinationUUID = _PanDestinationUUID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 84),
    _PanDestinationUUID_Type()
)
panDestinationUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationUUID.setStatus("current")


class _PanTunnel_Type(Integer32):
    """Custom type panTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("gre", 1),
          ("ipsec", 2),
          ("gtpu", 3),
          ("gtp", 4),
          ("vxlan", 5))
    )


_PanTunnel_Type.__name__ = "Integer32"
_PanTunnel_Object = MibScalar
panTunnel = _PanTunnel_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 85),
    _PanTunnel_Type()
)
panTunnel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTunnel.setStatus("current")


class _PanRuleUUID_Type(OctetString):
    """Custom type panRuleUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_PanRuleUUID_Type.__name__ = "OctetString"
_PanRuleUUID_Object = MibScalar
panRuleUUID = _PanRuleUUID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 86),
    _PanRuleUUID_Type()
)
panRuleUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRuleUUID.setStatus("current")
_PanTrafficBytes_Type = Counter64
_PanTrafficBytes_Object = MibScalar
panTrafficBytes = _PanTrafficBytes_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 100),
    _PanTrafficBytes_Type()
)
panTrafficBytes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficBytes.setStatus("current")
_PanTrafficPackets_Type = Counter32
_PanTrafficPackets_Object = MibScalar
panTrafficPackets = _PanTrafficPackets_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 101),
    _PanTrafficPackets_Type()
)
panTrafficPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficPackets.setStatus("current")


class _PanTrafficStartTime_Type(OctetString):
    """Custom type panTrafficStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficStartTime_Type.__name__ = "OctetString"
_PanTrafficStartTime_Object = MibScalar
panTrafficStartTime = _PanTrafficStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 102),
    _PanTrafficStartTime_Type()
)
panTrafficStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficStartTime.setStatus("current")
_PanTrafficElapsed_Type = TimeStamp
_PanTrafficElapsed_Object = MibScalar
panTrafficElapsed = _PanTrafficElapsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 103),
    _PanTrafficElapsed_Type()
)
panTrafficElapsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficElapsed.setStatus("current")


class _PanTrafficCategory_Type(OctetString):
    """Custom type panTrafficCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficCategory_Type.__name__ = "OctetString"
_PanTrafficCategory_Object = MibScalar
panTrafficCategory = _PanTrafficCategory_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 104),
    _PanTrafficCategory_Type()
)
panTrafficCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficCategory.setStatus("current")


class _PanTrafficSessionEndReason_Type(OctetString):
    """Custom type panTrafficSessionEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficSessionEndReason_Type.__name__ = "OctetString"
_PanTrafficSessionEndReason_Object = MibScalar
panTrafficSessionEndReason = _PanTrafficSessionEndReason_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 105),
    _PanTrafficSessionEndReason_Type()
)
panTrafficSessionEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficSessionEndReason.setStatus("current")
_PanTrafficTunnelID_Type = Counter64
_PanTrafficTunnelID_Object = MibScalar
panTrafficTunnelID = _PanTrafficTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 106),
    _PanTrafficTunnelID_Type()
)
panTrafficTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficTunnelID.setStatus("current")
_PanTrafficImsi_Type = Counter64
_PanTrafficImsi_Object = MibScalar
panTrafficImsi = _PanTrafficImsi_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 107),
    _PanTrafficImsi_Type()
)
panTrafficImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficImsi.setStatus("current")


class _PanTrafficMonitorTag_Type(OctetString):
    """Custom type panTrafficMonitorTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficMonitorTag_Type.__name__ = "OctetString"
_PanTrafficMonitorTag_Object = MibScalar
panTrafficMonitorTag = _PanTrafficMonitorTag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 108),
    _PanTrafficMonitorTag_Type()
)
panTrafficMonitorTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficMonitorTag.setStatus("current")


class _PanTrafficImei_Type(OctetString):
    """Custom type panTrafficImei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficImei_Type.__name__ = "OctetString"
_PanTrafficImei_Object = MibScalar
panTrafficImei = _PanTrafficImei_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 109),
    _PanTrafficImei_Type()
)
panTrafficImei.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficImei.setStatus("current")
_PanTrafficParentSessionId_Type = Counter32
_PanTrafficParentSessionId_Object = MibScalar
panTrafficParentSessionId = _PanTrafficParentSessionId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 110),
    _PanTrafficParentSessionId_Type()
)
panTrafficParentSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficParentSessionId.setStatus("current")
_PanTrafficParentStartTime_Type = Counter32
_PanTrafficParentStartTime_Object = MibScalar
panTrafficParentStartTime = _PanTrafficParentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 111),
    _PanTrafficParentStartTime_Type()
)
panTrafficParentStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficParentStartTime.setStatus("current")


class _PanConfigCmd_Type(OctetString):
    """Custom type panConfigCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PanConfigCmd_Type.__name__ = "OctetString"
_PanConfigCmd_Object = MibScalar
panConfigCmd = _PanConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 150),
    _PanConfigCmd_Type()
)
panConfigCmd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigCmd.setStatus("current")


class _PanConfigAdmin_Type(OctetString):
    """Custom type panConfigAdmin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanConfigAdmin_Type.__name__ = "OctetString"
_PanConfigAdmin_Object = MibScalar
panConfigAdmin = _PanConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 151),
    _PanConfigAdmin_Type()
)
panConfigAdmin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigAdmin.setStatus("current")


class _PanConfigClient_Type(OctetString):
    """Custom type panConfigClient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanConfigClient_Type.__name__ = "OctetString"
_PanConfigClient_Object = MibScalar
panConfigClient = _PanConfigClient_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 152),
    _PanConfigClient_Type()
)
panConfigClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigClient.setStatus("current")


class _PanConfigResult_Type(OctetString):
    """Custom type panConfigResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanConfigResult_Type.__name__ = "OctetString"
_PanConfigResult_Object = MibScalar
panConfigResult = _PanConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 153),
    _PanConfigResult_Type()
)
panConfigResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigResult.setStatus("current")


class _PanConfigPath_Type(OctetString):
    """Custom type panConfigPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PanConfigPath_Type.__name__ = "OctetString"
_PanConfigPath_Object = MibScalar
panConfigPath = _PanConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 154),
    _PanConfigPath_Type()
)
panConfigPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigPath.setStatus("current")


class _PanThreatId_Type(OctetString):
    """Custom type panThreatId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatId_Type.__name__ = "OctetString"
_PanThreatId_Object = MibScalar
panThreatId = _PanThreatId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 200),
    _PanThreatId_Type()
)
panThreatId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatId.setStatus("current")


class _PanThreatCategory_Type(OctetString):
    """Custom type panThreatCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatCategory_Type.__name__ = "OctetString"
_PanThreatCategory_Object = MibScalar
panThreatCategory = _PanThreatCategory_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 201),
    _PanThreatCategory_Type()
)
panThreatCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatCategory.setStatus("current")


class _PanThreatContentType_Type(OctetString):
    """Custom type panThreatContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatContentType_Type.__name__ = "OctetString"
_PanThreatContentType_Object = MibScalar
panThreatContentType = _PanThreatContentType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 202),
    _PanThreatContentType_Type()
)
panThreatContentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatContentType.setStatus("current")


class _PanThreatSeverity_Type(Integer32):
    """Custom type panThreatSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("critical", 5))
    )


_PanThreatSeverity_Type.__name__ = "Integer32"
_PanThreatSeverity_Object = MibScalar
panThreatSeverity = _PanThreatSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 203),
    _PanThreatSeverity_Type()
)
panThreatSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatSeverity.setStatus("current")


class _PanThreatDirection_Type(Integer32):
    """Custom type panThreatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client-to-server", 0),
          ("server-to-client", 1))
    )


_PanThreatDirection_Type.__name__ = "Integer32"
_PanThreatDirection_Object = MibScalar
panThreatDirection = _PanThreatDirection_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 204),
    _PanThreatDirection_Type()
)
panThreatDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatDirection.setStatus("current")


class _PanMiscellaneous_Type(OctetString):
    """Custom type panMiscellaneous based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanMiscellaneous_Type.__name__ = "OctetString"
_PanMiscellaneous_Object = MibScalar
panMiscellaneous = _PanMiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 205),
    _PanMiscellaneous_Type()
)
panMiscellaneous.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panMiscellaneous.setStatus("current")
_PanPcapId_Type = Counter64
_PanPcapId_Object = MibScalar
panPcapId = _PanPcapId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 206),
    _PanPcapId_Type()
)
panPcapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panPcapId.setStatus("current")


class _PanFileDigest_Type(OctetString):
    """Custom type panFileDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanFileDigest_Type.__name__ = "OctetString"
_PanFileDigest_Object = MibScalar
panFileDigest = _PanFileDigest_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 207),
    _PanFileDigest_Type()
)
panFileDigest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFileDigest.setStatus("current")


class _PanCloud_Type(OctetString):
    """Custom type panCloud based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanCloud_Type.__name__ = "OctetString"
_PanCloud_Object = MibScalar
panCloud = _PanCloud_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 208),
    _PanCloud_Type()
)
panCloud.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCloud.setStatus("current")
_PanUrlIndex_Type = Integer32
_PanUrlIndex_Object = MibScalar
panUrlIndex = _PanUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 209),
    _PanUrlIndex_Type()
)
panUrlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUrlIndex.setStatus("current")


class _PanUserAgent_Type(OctetString):
    """Custom type panUserAgent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanUserAgent_Type.__name__ = "OctetString"
_PanUserAgent_Object = MibScalar
panUserAgent = _PanUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 210),
    _PanUserAgent_Type()
)
panUserAgent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUserAgent.setStatus("current")


class _PanXff_Type(OctetString):
    """Custom type panXff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanXff_Type.__name__ = "OctetString"
_PanXff_Object = MibScalar
panXff = _PanXff_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 211),
    _PanXff_Type()
)
panXff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panXff.setStatus("current")


class _PanReferer_Type(OctetString):
    """Custom type panReferer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanReferer_Type.__name__ = "OctetString"
_PanReferer_Object = MibScalar
panReferer = _PanReferer_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 212),
    _PanReferer_Type()
)
panReferer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReferer.setStatus("current")


class _PanSender_Type(OctetString):
    """Custom type panSender based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanSender_Type.__name__ = "OctetString"
_PanSender_Object = MibScalar
panSender = _PanSender_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 213),
    _PanSender_Type()
)
panSender.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSender.setStatus("current")


class _PanSubject_Type(OctetString):
    """Custom type panSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanSubject_Type.__name__ = "OctetString"
_PanSubject_Object = MibScalar
panSubject = _PanSubject_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 214),
    _PanSubject_Type()
)
panSubject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSubject.setStatus("current")


class _PanRecipient_Type(OctetString):
    """Custom type panRecipient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanRecipient_Type.__name__ = "OctetString"
_PanRecipient_Object = MibScalar
panRecipient = _PanRecipient_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 215),
    _PanRecipient_Type()
)
panRecipient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRecipient.setStatus("current")


class _PanFileType_Type(OctetString):
    """Custom type panFileType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanFileType_Type.__name__ = "OctetString"
_PanFileType_Object = MibScalar
panFileType = _PanFileType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 216),
    _PanFileType_Type()
)
panFileType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFileType.setStatus("current")


class _PanReportId_Type(OctetString):
    """Custom type panReportId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanReportId_Type.__name__ = "OctetString"
_PanReportId_Object = MibScalar
panReportId = _PanReportId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 217),
    _PanReportId_Type()
)
panReportId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReportId.setStatus("current")
_PanHttpMethod_Type = Integer32
_PanHttpMethod_Object = MibScalar
panHttpMethod = _PanHttpMethod_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 218),
    _PanHttpMethod_Type()
)
panHttpMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHttpMethod.setStatus("current")
_PanThreatTunnelID_Type = Counter64
_PanThreatTunnelID_Object = MibScalar
panThreatTunnelID = _PanThreatTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 219),
    _PanThreatTunnelID_Type()
)
panThreatTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatTunnelID.setStatus("current")
_PanThreatImsi_Type = Counter64
_PanThreatImsi_Object = MibScalar
panThreatImsi = _PanThreatImsi_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 220),
    _PanThreatImsi_Type()
)
panThreatImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatImsi.setStatus("current")


class _PanThreatMonitorTag_Type(OctetString):
    """Custom type panThreatMonitorTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatMonitorTag_Type.__name__ = "OctetString"
_PanThreatMonitorTag_Object = MibScalar
panThreatMonitorTag = _PanThreatMonitorTag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 221),
    _PanThreatMonitorTag_Type()
)
panThreatMonitorTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatMonitorTag.setStatus("current")


class _PanThreatImei_Type(OctetString):
    """Custom type panThreatImei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatImei_Type.__name__ = "OctetString"
_PanThreatImei_Object = MibScalar
panThreatImei = _PanThreatImei_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 222),
    _PanThreatImei_Type()
)
panThreatImei.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatImei.setStatus("current")
_PanThreatParentSessionId_Type = Counter32
_PanThreatParentSessionId_Object = MibScalar
panThreatParentSessionId = _PanThreatParentSessionId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 223),
    _PanThreatParentSessionId_Type()
)
panThreatParentSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatParentSessionId.setStatus("current")
_PanThreatParentStartTime_Type = Counter32
_PanThreatParentStartTime_Object = MibScalar
panThreatParentStartTime = _PanThreatParentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 224),
    _PanThreatParentStartTime_Type()
)
panThreatParentStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatParentStartTime.setStatus("current")
_PanThrCategory_Type = Counter32
_PanThrCategory_Object = MibScalar
panThrCategory = _PanThrCategory_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 225),
    _PanThrCategory_Type()
)
panThrCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThrCategory.setStatus("current")


class _PanHipSourceUser_Type(OctetString):
    """Custom type panHipSourceUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanHipSourceUser_Type.__name__ = "OctetString"
_PanHipSourceUser_Object = MibScalar
panHipSourceUser = _PanHipSourceUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 250),
    _PanHipSourceUser_Type()
)
panHipSourceUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceUser.setStatus("current")


class _PanHipMachineName_Type(OctetString):
    """Custom type panHipMachineName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanHipMachineName_Type.__name__ = "OctetString"
_PanHipMachineName_Object = MibScalar
panHipMachineName = _PanHipMachineName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 251),
    _PanHipMachineName_Type()
)
panHipMachineName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMachineName.setStatus("current")
_PanHipSource_Type = IpAddress
_PanHipSource_Object = MibScalar
panHipSource = _PanHipSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 252),
    _PanHipSource_Type()
)
panHipSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSource.setStatus("current")


class _PanHipMatch_Type(OctetString):
    """Custom type panHipMatch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipMatch_Type.__name__ = "OctetString"
_PanHipMatch_Object = MibScalar
panHipMatch = _PanHipMatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 253),
    _PanHipMatch_Type()
)
panHipMatch.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMatch.setStatus("current")


class _PanHipMatchType_Type(OctetString):
    """Custom type panHipMatchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipMatchType_Type.__name__ = "OctetString"
_PanHipMatchType_Object = MibScalar
panHipMatchType = _PanHipMatchType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 254),
    _PanHipMatchType_Type()
)
panHipMatchType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMatchType.setStatus("current")
_PanHipRepeatCount_Type = Counter32
_PanHipRepeatCount_Object = MibScalar
panHipRepeatCount = _PanHipRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 255),
    _PanHipRepeatCount_Type()
)
panHipRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipRepeatCount.setStatus("current")


class _PanHipOS_Type(OctetString):
    """Custom type panHipOS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipOS_Type.__name__ = "OctetString"
_PanHipOS_Object = MibScalar
panHipOS = _PanHipOS_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 256),
    _PanHipOS_Type()
)
panHipOS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipOS.setStatus("current")
_PanHipSourceInetAddrType_Type = InetAddressType
_PanHipSourceInetAddrType_Object = MibScalar
panHipSourceInetAddrType = _PanHipSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 257),
    _PanHipSourceInetAddrType_Type()
)
panHipSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceInetAddrType.setStatus("current")
_PanHipSourceInetAddr_Type = InetAddress
_PanHipSourceInetAddr_Object = MibScalar
panHipSourceInetAddr = _PanHipSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 258),
    _PanHipSourceInetAddr_Type()
)
panHipSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceInetAddr.setStatus("current")
_PanHipSourceIPv6_Type = IpAddress
_PanHipSourceIPv6_Object = MibScalar
panHipSourceIPv6 = _PanHipSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 259),
    _PanHipSourceIPv6_Type()
)
panHipSourceIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceIPv6.setStatus("current")
_PanHipSourceIPv6InetAddrType_Type = InetAddressType
_PanHipSourceIPv6InetAddrType_Object = MibScalar
panHipSourceIPv6InetAddrType = _PanHipSourceIPv6InetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 260),
    _PanHipSourceIPv6InetAddrType_Type()
)
panHipSourceIPv6InetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceIPv6InetAddrType.setStatus("current")
_PanHipSourceIPv6InetAddr_Type = InetAddress
_PanHipSourceIPv6InetAddr_Object = MibScalar
panHipSourceIPv6InetAddr = _PanHipSourceIPv6InetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 261),
    _PanHipSourceIPv6InetAddr_Type()
)
panHipSourceIPv6InetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceIPv6InetAddr.setStatus("current")


class _PanSystemEventId_Type(OctetString):
    """Custom type panSystemEventId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSystemEventId_Type.__name__ = "OctetString"
_PanSystemEventId_Object = MibScalar
panSystemEventId = _PanSystemEventId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 300),
    _PanSystemEventId_Type()
)
panSystemEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemEventId.setStatus("current")


class _PanSystemObject_Type(OctetString):
    """Custom type panSystemObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSystemObject_Type.__name__ = "OctetString"
_PanSystemObject_Object = MibScalar
panSystemObject = _PanSystemObject_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 301),
    _PanSystemObject_Type()
)
panSystemObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemObject.setStatus("current")


class _PanSystemModule_Type(OctetString):
    """Custom type panSystemModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSystemModule_Type.__name__ = "OctetString"
_PanSystemModule_Object = MibScalar
panSystemModule = _PanSystemModule_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 302),
    _PanSystemModule_Type()
)
panSystemModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemModule.setStatus("current")


class _PanSystemSeverity_Type(Integer32):
    """Custom type panSystemSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("critical", 5))
    )


_PanSystemSeverity_Type.__name__ = "Integer32"
_PanSystemSeverity_Object = MibScalar
panSystemSeverity = _PanSystemSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 303),
    _PanSystemSeverity_Type()
)
panSystemSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemSeverity.setStatus("current")


class _PanSystemDescription_Type(OctetString):
    """Custom type panSystemDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_PanSystemDescription_Type.__name__ = "OctetString"
_PanSystemDescription_Object = MibScalar
panSystemDescription = _PanSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 304),
    _PanSystemDescription_Type()
)
panSystemDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemDescription.setStatus("current")


class _PanCorrDG1_Type(OctetString):
    """Custom type panCorrDG1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG1_Type.__name__ = "OctetString"
_PanCorrDG1_Object = MibScalar
panCorrDG1 = _PanCorrDG1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 350),
    _PanCorrDG1_Type()
)
panCorrDG1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG1.setStatus("current")


class _PanCorrDG2_Type(OctetString):
    """Custom type panCorrDG2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG2_Type.__name__ = "OctetString"
_PanCorrDG2_Object = MibScalar
panCorrDG2 = _PanCorrDG2_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 351),
    _PanCorrDG2_Type()
)
panCorrDG2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG2.setStatus("current")


class _PanCorrDG3_Type(OctetString):
    """Custom type panCorrDG3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG3_Type.__name__ = "OctetString"
_PanCorrDG3_Object = MibScalar
panCorrDG3 = _PanCorrDG3_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 352),
    _PanCorrDG3_Type()
)
panCorrDG3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG3.setStatus("current")


class _PanCorrDG4_Type(OctetString):
    """Custom type panCorrDG4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG4_Type.__name__ = "OctetString"
_PanCorrDG4_Object = MibScalar
panCorrDG4 = _PanCorrDG4_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 353),
    _PanCorrDG4_Type()
)
panCorrDG4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG4.setStatus("current")


class _PanCorrObjName_Type(OctetString):
    """Custom type panCorrObjName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrObjName_Type.__name__ = "OctetString"
_PanCorrObjName_Object = MibScalar
panCorrObjName = _PanCorrObjName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 354),
    _PanCorrObjName_Type()
)
panCorrObjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrObjName.setStatus("current")
_PanCorrObjID_Type = Integer32
_PanCorrObjID_Object = MibScalar
panCorrObjID = _PanCorrObjID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 355),
    _PanCorrObjID_Type()
)
panCorrObjID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrObjID.setStatus("current")
_PanCorrSeverity_Type = Integer32
_PanCorrSeverity_Object = MibScalar
panCorrSeverity = _PanCorrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 356),
    _PanCorrSeverity_Type()
)
panCorrSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrSeverity.setStatus("current")


class _PanCorrEvidence_Type(OctetString):
    """Custom type panCorrEvidence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanCorrEvidence_Type.__name__ = "OctetString"
_PanCorrEvidence_Object = MibScalar
panCorrEvidence = _PanCorrEvidence_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 357),
    _PanCorrEvidence_Type()
)
panCorrEvidence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrEvidence.setStatus("current")
_PanGtpTunnelID_Type = Counter64
_PanGtpTunnelID_Object = MibScalar
panGtpTunnelID = _PanGtpTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 400),
    _PanGtpTunnelID_Type()
)
panGtpTunnelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpTunnelID.setStatus("current")
_PanGtpImsi_Type = Counter64
_PanGtpImsi_Object = MibScalar
panGtpImsi = _PanGtpImsi_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 401),
    _PanGtpImsi_Type()
)
panGtpImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpImsi.setStatus("current")


class _PanGtpMonitorTag_Type(OctetString):
    """Custom type panGtpMonitorTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpMonitorTag_Type.__name__ = "OctetString"
_PanGtpMonitorTag_Object = MibScalar
panGtpMonitorTag = _PanGtpMonitorTag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 402),
    _PanGtpMonitorTag_Type()
)
panGtpMonitorTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMonitorTag.setStatus("current")


class _PanGtpImei_Type(OctetString):
    """Custom type panGtpImei based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpImei_Type.__name__ = "OctetString"
_PanGtpImei_Object = MibScalar
panGtpImei = _PanGtpImei_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 403),
    _PanGtpImei_Type()
)
panGtpImei.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpImei.setStatus("current")
_PanGtpParentSessionId_Type = Counter32
_PanGtpParentSessionId_Object = MibScalar
panGtpParentSessionId = _PanGtpParentSessionId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 404),
    _PanGtpParentSessionId_Type()
)
panGtpParentSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpParentSessionId.setStatus("current")
_PanGtpParentStartTime_Type = Counter32
_PanGtpParentStartTime_Object = MibScalar
panGtpParentStartTime = _PanGtpParentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 405),
    _PanGtpParentStartTime_Type()
)
panGtpParentStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpParentStartTime.setStatus("current")


class _PanGtpMsisdn_Type(OctetString):
    """Custom type panGtpMsisdn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGtpMsisdn_Type.__name__ = "OctetString"
_PanGtpMsisdn_Object = MibScalar
panGtpMsisdn = _PanGtpMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 406),
    _PanGtpMsisdn_Type()
)
panGtpMsisdn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMsisdn.setStatus("current")


class _PanGtpApn_Type(OctetString):
    """Custom type panGtpApn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanGtpApn_Type.__name__ = "OctetString"
_PanGtpApn_Object = MibScalar
panGtpApn = _PanGtpApn_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 407),
    _PanGtpApn_Type()
)
panGtpApn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpApn.setStatus("current")


class _PanGtpRat_Type(OctetString):
    """Custom type panGtpRat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGtpRat_Type.__name__ = "OctetString"
_PanGtpRat_Object = MibScalar
panGtpRat = _PanGtpRat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 408),
    _PanGtpRat_Type()
)
panGtpRat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpRat.setStatus("current")


class _PanGtpMsgType_Type(OctetString):
    """Custom type panGtpMsgType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanGtpMsgType_Type.__name__ = "OctetString"
_PanGtpMsgType_Object = MibScalar
panGtpMsgType = _PanGtpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 409),
    _PanGtpMsgType_Type()
)
panGtpMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMsgType.setStatus("current")
_PanGtpEndipaddrInetAddrType_Type = InetAddressType
_PanGtpEndipaddrInetAddrType_Object = MibScalar
panGtpEndipaddrInetAddrType = _PanGtpEndipaddrInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 410),
    _PanGtpEndipaddrInetAddrType_Type()
)
panGtpEndipaddrInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpEndipaddrInetAddrType.setStatus("current")
_PanGtpEndIpAddr_Type = InetAddress
_PanGtpEndIpAddr_Object = MibScalar
panGtpEndIpAddr = _PanGtpEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 411),
    _PanGtpEndIpAddr_Type()
)
panGtpEndIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpEndIpAddr.setStatus("current")
_PanGtpTeid1_Type = Counter32
_PanGtpTeid1_Object = MibScalar
panGtpTeid1 = _PanGtpTeid1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 412),
    _PanGtpTeid1_Type()
)
panGtpTeid1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpTeid1.setStatus("current")
_PanGtpTeid2_Type = Counter32
_PanGtpTeid2_Object = MibScalar
panGtpTeid2 = _PanGtpTeid2_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 413),
    _PanGtpTeid2_Type()
)
panGtpTeid2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpTeid2.setStatus("current")


class _PanGtpInterface_Type(OctetString):
    """Custom type panGtpInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGtpInterface_Type.__name__ = "OctetString"
_PanGtpInterface_Object = MibScalar
panGtpInterface = _PanGtpInterface_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 414),
    _PanGtpInterface_Type()
)
panGtpInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpInterface.setStatus("current")


class _PanGtpCauseCode_Type(OctetString):
    """Custom type panGtpCauseCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpCauseCode_Type.__name__ = "OctetString"
_PanGtpCauseCode_Object = MibScalar
panGtpCauseCode = _PanGtpCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 415),
    _PanGtpCauseCode_Type()
)
panGtpCauseCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpCauseCode.setStatus("current")


class _PanGtpEventType_Type(OctetString):
    """Custom type panGtpEventType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanGtpEventType_Type.__name__ = "OctetString"
_PanGtpEventType_Object = MibScalar
panGtpEventType = _PanGtpEventType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 416),
    _PanGtpEventType_Type()
)
panGtpEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpEventType.setStatus("current")


class _PanGtpSeverity_Type(Integer32):
    """Custom type panGtpSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("critical", 5))
    )


_PanGtpSeverity_Type.__name__ = "Integer32"
_PanGtpSeverity_Object = MibScalar
panGtpSeverity = _PanGtpSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 417),
    _PanGtpSeverity_Type()
)
panGtpSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpSeverity.setStatus("current")
_PanGtpMcc_Type = Counter32
_PanGtpMcc_Object = MibScalar
panGtpMcc = _PanGtpMcc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 418),
    _PanGtpMcc_Type()
)
panGtpMcc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMcc.setStatus("current")
_PanGtpMnc_Type = Counter32
_PanGtpMnc_Object = MibScalar
panGtpMnc = _PanGtpMnc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 419),
    _PanGtpMnc_Type()
)
panGtpMnc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMnc.setStatus("current")
_PanGtpAreaCode_Type = Counter32
_PanGtpAreaCode_Object = MibScalar
panGtpAreaCode = _PanGtpAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 420),
    _PanGtpAreaCode_Type()
)
panGtpAreaCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpAreaCode.setStatus("current")
_PanGtpCellId_Type = Counter32
_PanGtpCellId_Object = MibScalar
panGtpCellId = _PanGtpCellId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 421),
    _PanGtpCellId_Type()
)
panGtpCellId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpCellId.setStatus("current")
_PanGtpEventCode_Type = Counter32
_PanGtpEventCode_Object = MibScalar
panGtpEventCode = _PanGtpEventCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 422),
    _PanGtpEventCode_Type()
)
panGtpEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpEventCode.setStatus("current")
_PanGtpBytes_Type = Counter64
_PanGtpBytes_Object = MibScalar
panGtpBytes = _PanGtpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 423),
    _PanGtpBytes_Type()
)
panGtpBytes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpBytes.setStatus("current")
_PanGtpPackets_Type = Counter32
_PanGtpPackets_Object = MibScalar
panGtpPackets = _PanGtpPackets_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 424),
    _PanGtpPackets_Type()
)
panGtpPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpPackets.setStatus("current")
_PanGtpMaxEncap_Type = Counter32
_PanGtpMaxEncap_Object = MibScalar
panGtpMaxEncap = _PanGtpMaxEncap_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 425),
    _PanGtpMaxEncap_Type()
)
panGtpMaxEncap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpMaxEncap.setStatus("current")
_PanGtpUnknownProto_Type = Counter32
_PanGtpUnknownProto_Object = MibScalar
panGtpUnknownProto = _PanGtpUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 426),
    _PanGtpUnknownProto_Type()
)
panGtpUnknownProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpUnknownProto.setStatus("current")
_PanGtpStrictCheck_Type = Counter32
_PanGtpStrictCheck_Object = MibScalar
panGtpStrictCheck = _PanGtpStrictCheck_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 427),
    _PanGtpStrictCheck_Type()
)
panGtpStrictCheck.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpStrictCheck.setStatus("current")
_PanGtpTunnelFragment_Type = Counter32
_PanGtpTunnelFragment_Object = MibScalar
panGtpTunnelFragment = _PanGtpTunnelFragment_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 428),
    _PanGtpTunnelFragment_Type()
)
panGtpTunnelFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpTunnelFragment.setStatus("current")
_PanGtpSessionsCreated_Type = Counter32
_PanGtpSessionsCreated_Object = MibScalar
panGtpSessionsCreated = _PanGtpSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 429),
    _PanGtpSessionsCreated_Type()
)
panGtpSessionsCreated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpSessionsCreated.setStatus("current")
_PanGtpSessionsClosed_Type = Counter32
_PanGtpSessionsClosed_Object = MibScalar
panGtpSessionsClosed = _PanGtpSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 430),
    _PanGtpSessionsClosed_Type()
)
panGtpSessionsClosed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpSessionsClosed.setStatus("current")


class _PanGtpSessionEndReason_Type(OctetString):
    """Custom type panGtpSessionEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpSessionEndReason_Type.__name__ = "OctetString"
_PanGtpSessionEndReason_Object = MibScalar
panGtpSessionEndReason = _PanGtpSessionEndReason_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 431),
    _PanGtpSessionEndReason_Type()
)
panGtpSessionEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpSessionEndReason.setStatus("current")


class _PanGtpActionSource_Type(OctetString):
    """Custom type panGtpActionSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpActionSource_Type.__name__ = "OctetString"
_PanGtpActionSource_Object = MibScalar
panGtpActionSource = _PanGtpActionSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 432),
    _PanGtpActionSource_Type()
)
panGtpActionSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpActionSource.setStatus("current")


class _PanGtpStartTime_Type(OctetString):
    """Custom type panGtpStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGtpStartTime_Type.__name__ = "OctetString"
_PanGtpStartTime_Object = MibScalar
panGtpStartTime = _PanGtpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 433),
    _PanGtpStartTime_Type()
)
panGtpStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpStartTime.setStatus("current")
_PanGtpElapsed_Type = TimeStamp
_PanGtpElapsed_Object = MibScalar
panGtpElapsed = _PanGtpElapsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 434),
    _PanGtpElapsed_Type()
)
panGtpElapsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpElapsed.setStatus("current")


class _PanGtpTCIRule_Type(OctetString):
    """Custom type panGtpTCIRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanGtpTCIRule_Type.__name__ = "OctetString"
_PanGtpTCIRule_Object = MibScalar
panGtpTCIRule = _PanGtpTCIRule_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 435),
    _PanGtpTCIRule_Type()
)
panGtpTCIRule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpTCIRule.setStatus("current")
_PanGtpRemoteUserIpInetAddrType_Type = InetAddressType
_PanGtpRemoteUserIpInetAddrType_Object = MibScalar
panGtpRemoteUserIpInetAddrType = _PanGtpRemoteUserIpInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 436),
    _PanGtpRemoteUserIpInetAddrType_Type()
)
panGtpRemoteUserIpInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpRemoteUserIpInetAddrType.setStatus("current")
_PanGtpRemoteUserIp_Type = InetAddress
_PanGtpRemoteUserIp_Object = MibScalar
panGtpRemoteUserIp = _PanGtpRemoteUserIp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 437),
    _PanGtpRemoteUserIp_Type()
)
panGtpRemoteUserIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpRemoteUserIp.setStatus("current")
_PanGtpRemoteUserId_Type = Counter64
_PanGtpRemoteUserId_Object = MibScalar
panGtpRemoteUserId = _PanGtpRemoteUserId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 438),
    _PanGtpRemoteUserId_Type()
)
panGtpRemoteUserId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGtpRemoteUserId.setStatus("current")
_PanUseridSourceInetAddrType_Type = InetAddressType
_PanUseridSourceInetAddrType_Object = MibScalar
panUseridSourceInetAddrType = _PanUseridSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 500),
    _PanUseridSourceInetAddrType_Type()
)
panUseridSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridSourceInetAddrType.setStatus("current")
_PanUseridSourceInetAddr_Type = InetAddress
_PanUseridSourceInetAddr_Object = MibScalar
panUseridSourceInetAddr = _PanUseridSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 501),
    _PanUseridSourceInetAddr_Type()
)
panUseridSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridSourceInetAddr.setStatus("current")


class _PanUseridUser_Type(OctetString):
    """Custom type panUseridUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanUseridUser_Type.__name__ = "OctetString"
_PanUseridUser_Object = MibScalar
panUseridUser = _PanUseridUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 502),
    _PanUseridUser_Type()
)
panUseridUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridUser.setStatus("current")


class _PanUseridDataSourceName_Type(OctetString):
    """Custom type panUseridDataSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanUseridDataSourceName_Type.__name__ = "OctetString"
_PanUseridDataSourceName_Object = MibScalar
panUseridDataSourceName = _PanUseridDataSourceName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 503),
    _PanUseridDataSourceName_Type()
)
panUseridDataSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridDataSourceName.setStatus("current")
_PanUseridEventID_Type = Counter32
_PanUseridEventID_Object = MibScalar
panUseridEventID = _PanUseridEventID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 504),
    _PanUseridEventID_Type()
)
panUseridEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridEventID.setStatus("current")
_PanUseridRepeatCount_Type = Counter32
_PanUseridRepeatCount_Object = MibScalar
panUseridRepeatCount = _PanUseridRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 505),
    _PanUseridRepeatCount_Type()
)
panUseridRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridRepeatCount.setStatus("current")
_PanUseridTimeout_Type = Counter32
_PanUseridTimeout_Object = MibScalar
panUseridTimeout = _PanUseridTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 506),
    _PanUseridTimeout_Type()
)
panUseridTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridTimeout.setStatus("current")
_PanUseridBeginport_Type = Counter32
_PanUseridBeginport_Object = MibScalar
panUseridBeginport = _PanUseridBeginport_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 507),
    _PanUseridBeginport_Type()
)
panUseridBeginport.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridBeginport.setStatus("current")
_PanUseridEndport_Type = Counter32
_PanUseridEndport_Object = MibScalar
panUseridEndport = _PanUseridEndport_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 508),
    _PanUseridEndport_Type()
)
panUseridEndport.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridEndport.setStatus("current")


class _PanUseridDataSource_Type(Integer32):
    """Custom type panUseridDataSource based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("agent", 1),
          ("tsAgent", 2),
          ("eventLog", 3),
          ("probing", 4),
          ("serverSessionMonitor", 5),
          ("captivePortal", 6),
          ("vpnClient", 7),
          ("xmlApi", 8),
          ("ha", 9),
          ("activeDirectory", 10),
          ("eDirectory", 11),
          ("syslog", 12))
    )


_PanUseridDataSource_Type.__name__ = "Integer32"
_PanUseridDataSource_Object = MibScalar
panUseridDataSource = _PanUseridDataSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 509),
    _PanUseridDataSource_Type()
)
panUseridDataSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridDataSource.setStatus("current")


class _PanUseridDataSourceType_Type(Integer32):
    """Custom type panUseridDataSourceType based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("directoryServer", 1),
          ("exchangeServer", 2),
          ("edirectoryServer", 3),
          ("wmiProbing", 4),
          ("netbiosProbing", 5),
          ("clientCert", 6),
          ("sso", 7),
          ("kerbos", 8),
          ("authenticate", 9),
          ("globalprotect", 10),
          ("vpnClient", 11))
    )


_PanUseridDataSourceType_Type.__name__ = "Integer32"
_PanUseridDataSourceType_Object = MibScalar
panUseridDataSourceType = _PanUseridDataSourceType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 510),
    _PanUseridDataSourceType_Type()
)
panUseridDataSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridDataSourceType.setStatus("current")


class _PanUseridFactorType_Type(OctetString):
    """Custom type panUseridFactorType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanUseridFactorType_Type.__name__ = "OctetString"
_PanUseridFactorType_Object = MibScalar
panUseridFactorType = _PanUseridFactorType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 511),
    _PanUseridFactorType_Type()
)
panUseridFactorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridFactorType.setStatus("current")


class _PanUseridFactorTime_Type(OctetString):
    """Custom type panUseridFactorTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanUseridFactorTime_Type.__name__ = "OctetString"
_PanUseridFactorTime_Object = MibScalar
panUseridFactorTime = _PanUseridFactorTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 512),
    _PanUseridFactorTime_Type()
)
panUseridFactorTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridFactorTime.setStatus("current")
_PanUseridFactorNo_Type = Counter32
_PanUseridFactorNo_Object = MibScalar
panUseridFactorNo = _PanUseridFactorNo_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 513),
    _PanUseridFactorNo_Type()
)
panUseridFactorNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUseridFactorNo.setStatus("current")
_PanAuthSourceInetAddrType_Type = InetAddressType
_PanAuthSourceInetAddrType_Object = MibScalar
panAuthSourceInetAddrType = _PanAuthSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 600),
    _PanAuthSourceInetAddrType_Type()
)
panAuthSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthSourceInetAddrType.setStatus("current")
_PanAuthSourceInetAddr_Type = InetAddress
_PanAuthSourceInetAddr_Object = MibScalar
panAuthSourceInetAddr = _PanAuthSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 601),
    _PanAuthSourceInetAddr_Type()
)
panAuthSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthSourceInetAddr.setStatus("current")


class _PanAuthUser_Type(OctetString):
    """Custom type panAuthUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanAuthUser_Type.__name__ = "OctetString"
_PanAuthUser_Object = MibScalar
panAuthUser = _PanAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 602),
    _PanAuthUser_Type()
)
panAuthUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthUser.setStatus("current")


class _PanAuthNormalizeUser_Type(OctetString):
    """Custom type panAuthNormalizeUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanAuthNormalizeUser_Type.__name__ = "OctetString"
_PanAuthNormalizeUser_Object = MibScalar
panAuthNormalizeUser = _PanAuthNormalizeUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 603),
    _PanAuthNormalizeUser_Type()
)
panAuthNormalizeUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthNormalizeUser.setStatus("current")


class _PanAuthObject_Type(OctetString):
    """Custom type panAuthObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAuthObject_Type.__name__ = "OctetString"
_PanAuthObject_Object = MibScalar
panAuthObject = _PanAuthObject_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 604),
    _PanAuthObject_Type()
)
panAuthObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthObject.setStatus("current")


class _PanAuthPolicy_Type(OctetString):
    """Custom type panAuthPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAuthPolicy_Type.__name__ = "OctetString"
_PanAuthPolicy_Object = MibScalar
panAuthPolicy = _PanAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 605),
    _PanAuthPolicy_Type()
)
panAuthPolicy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthPolicy.setStatus("current")
_PanAuthRepeatCount_Type = Counter32
_PanAuthRepeatCount_Object = MibScalar
panAuthRepeatCount = _PanAuthRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 606),
    _PanAuthRepeatCount_Type()
)
panAuthRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthRepeatCount.setStatus("current")
_PanAuthID_Type = Counter64
_PanAuthID_Object = MibScalar
panAuthID = _PanAuthID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 607),
    _PanAuthID_Type()
)
panAuthID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthID.setStatus("current")


class _PanAuthVendor_Type(OctetString):
    """Custom type panAuthVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAuthVendor_Type.__name__ = "OctetString"
_PanAuthVendor_Object = MibScalar
panAuthVendor = _PanAuthVendor_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 608),
    _PanAuthVendor_Type()
)
panAuthVendor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthVendor.setStatus("current")


class _PanAuthLogForwardingProfile_Type(OctetString):
    """Custom type panAuthLogForwardingProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAuthLogForwardingProfile_Type.__name__ = "OctetString"
_PanAuthLogForwardingProfile_Object = MibScalar
panAuthLogForwardingProfile = _PanAuthLogForwardingProfile_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 609),
    _PanAuthLogForwardingProfile_Type()
)
panAuthLogForwardingProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthLogForwardingProfile.setStatus("current")


class _PanAuthClientType_Type(Integer32):
    """Custom type panAuthClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adminui", 0),
          ("cli", 1),
          ("globalprotectPortal", 2),
          ("globalprotectGateway", 3),
          ("clientlessVpn", 4),
          ("authenticationPortal", 5))
    )


_PanAuthClientType_Type.__name__ = "Integer32"
_PanAuthClientType_Object = MibScalar
panAuthClientType = _PanAuthClientType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 610),
    _PanAuthClientType_Type()
)
panAuthClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthClientType.setStatus("current")


class _PanAuthDescription_Type(OctetString):
    """Custom type panAuthDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_PanAuthDescription_Type.__name__ = "OctetString"
_PanAuthDescription_Object = MibScalar
panAuthDescription = _PanAuthDescription_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 611),
    _PanAuthDescription_Type()
)
panAuthDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthDescription.setStatus("current")


class _PanAuthServerProfile_Type(OctetString):
    """Custom type panAuthServerProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAuthServerProfile_Type.__name__ = "OctetString"
_PanAuthServerProfile_Object = MibScalar
panAuthServerProfile = _PanAuthServerProfile_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 612),
    _PanAuthServerProfile_Type()
)
panAuthServerProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthServerProfile.setStatus("current")


class _PanAuthEvent_Type(Integer32):
    """Custom type panAuthEvent based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failure", 1),
          ("userPasswordFailure", 2),
          ("userIsLocked", 3),
          ("userNotAllowed", 4),
          ("invalidCertificate", 5),
          ("passwordExpired", 6),
          ("kerberosSingleSignOnFailed", 7),
          ("samlSingleSignOnFailed", 8),
          ("mfaFailed", 9),
          ("timeout", 10))
    )


_PanAuthEvent_Type.__name__ = "Integer32"
_PanAuthEvent_Object = MibScalar
panAuthEvent = _PanAuthEvent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 613),
    _PanAuthEvent_Type()
)
panAuthEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthEvent.setStatus("current")
_PanAuthFactorNo_Type = Counter32
_PanAuthFactorNo_Object = MibScalar
panAuthFactorNo = _PanAuthFactorNo_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 614),
    _PanAuthFactorNo_Type()
)
panAuthFactorNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthFactorNo.setStatus("current")


class _PanAuthProto_Type(Integer32):
    """Custom type panAuthProto based on Integer32"""
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
        *(("peapWithEapGtc", 0),
          ("peapMschapv2", 1),
          ("ttlsPap", 2),
          ("pap", 3),
          ("chap", 4))
    )


_PanAuthProto_Type.__name__ = "Integer32"
_PanAuthProto_Object = MibScalar
panAuthProto = _PanAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 615),
    _PanAuthProto_Type()
)
panAuthProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAuthProto.setStatus("current")
_PanSctpAssocId_Type = Counter64
_PanSctpAssocId_Object = MibScalar
panSctpAssocId = _PanSctpAssocId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 700),
    _PanSctpAssocId_Type()
)
panSctpAssocId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpAssocId.setStatus("current")


class _PanSctpPpid_Type(OctetString):
    """Custom type panSctpPpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSctpPpid_Type.__name__ = "OctetString"
_PanSctpPpid_Object = MibScalar
panSctpPpid = _PanSctpPpid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 701),
    _PanSctpPpid_Type()
)
panSctpPpid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpPpid.setStatus("current")


class _PanSctpSeverity_Type(Integer32):
    """Custom type panSctpSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4),
          ("critical", 5))
    )


_PanSctpSeverity_Type.__name__ = "Integer32"
_PanSctpSeverity_Object = MibScalar
panSctpSeverity = _PanSctpSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 702),
    _PanSctpSeverity_Type()
)
panSctpSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpSeverity.setStatus("current")


class _PanSctpChunkType_Type(OctetString):
    """Custom type panSctpChunkType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSctpChunkType_Type.__name__ = "OctetString"
_PanSctpChunkType_Object = MibScalar
panSctpChunkType = _PanSctpChunkType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 703),
    _PanSctpChunkType_Type()
)
panSctpChunkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpChunkType.setStatus("current")


class _PanSctpEventType_Type(OctetString):
    """Custom type panSctpEventType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSctpEventType_Type.__name__ = "OctetString"
_PanSctpEventType_Object = MibScalar
panSctpEventType = _PanSctpEventType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 704),
    _PanSctpEventType_Type()
)
panSctpEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpEventType.setStatus("current")
_PanSctpEventCode_Type = Integer32
_PanSctpEventCode_Object = MibScalar
panSctpEventCode = _PanSctpEventCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 705),
    _PanSctpEventCode_Type()
)
panSctpEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpEventCode.setStatus("current")
_PanSctpVerifTag1_Type = Counter32
_PanSctpVerifTag1_Object = MibScalar
panSctpVerifTag1 = _PanSctpVerifTag1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 706),
    _PanSctpVerifTag1_Type()
)
panSctpVerifTag1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpVerifTag1.setStatus("current")
_PanSctpVerifTag2_Type = Counter32
_PanSctpVerifTag2_Object = MibScalar
panSctpVerifTag2 = _PanSctpVerifTag2_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 707),
    _PanSctpVerifTag2_Type()
)
panSctpVerifTag2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpVerifTag2.setStatus("current")


class _PanSctpCauseCode_Type(OctetString):
    """Custom type panSctpCauseCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSctpCauseCode_Type.__name__ = "OctetString"
_PanSctpCauseCode_Object = MibScalar
panSctpCauseCode = _PanSctpCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 708),
    _PanSctpCauseCode_Type()
)
panSctpCauseCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpCauseCode.setStatus("current")


class _PanSctpDiamAppId_Type(OctetString):
    """Custom type panSctpDiamAppId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSctpDiamAppId_Type.__name__ = "OctetString"
_PanSctpDiamAppId_Object = MibScalar
panSctpDiamAppId = _PanSctpDiamAppId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 709),
    _PanSctpDiamAppId_Type()
)
panSctpDiamAppId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpDiamAppId.setStatus("current")


class _PanSctpDiamCmdCode_Type(OctetString):
    """Custom type panSctpDiamCmdCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSctpDiamCmdCode_Type.__name__ = "OctetString"
_PanSctpDiamCmdCode_Object = MibScalar
panSctpDiamCmdCode = _PanSctpDiamCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 710),
    _PanSctpDiamCmdCode_Type()
)
panSctpDiamCmdCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpDiamCmdCode.setStatus("current")
_PanSctpDiamAvpCode_Type = Counter32
_PanSctpDiamAvpCode_Object = MibScalar
panSctpDiamAvpCode = _PanSctpDiamAvpCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 711),
    _PanSctpDiamAvpCode_Type()
)
panSctpDiamAvpCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpDiamAvpCode.setStatus("current")
_PanSctpStreamId_Type = Counter32
_PanSctpStreamId_Object = MibScalar
panSctpStreamId = _PanSctpStreamId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 712),
    _PanSctpStreamId_Type()
)
panSctpStreamId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpStreamId.setStatus("current")


class _PanSctpOpCode_Type(OctetString):
    """Custom type panSctpOpCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSctpOpCode_Type.__name__ = "OctetString"
_PanSctpOpCode_Object = MibScalar
panSctpOpCode = _PanSctpOpCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 713),
    _PanSctpOpCode_Type()
)
panSctpOpCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpOpCode.setStatus("current")


class _PanSctpCallingSSN_Type(OctetString):
    """Custom type panSctpCallingSSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSctpCallingSSN_Type.__name__ = "OctetString"
_PanSctpCallingSSN_Object = MibScalar
panSctpCallingSSN = _PanSctpCallingSSN_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 714),
    _PanSctpCallingSSN_Type()
)
panSctpCallingSSN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpCallingSSN.setStatus("current")


class _PanSctpCallingGT_Type(OctetString):
    """Custom type panSctpCallingGT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PanSctpCallingGT_Type.__name__ = "OctetString"
_PanSctpCallingGT_Object = MibScalar
panSctpCallingGT = _PanSctpCallingGT_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 715),
    _PanSctpCallingGT_Type()
)
panSctpCallingGT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpCallingGT.setStatus("current")


class _PanSctpEndReason_Type(OctetString):
    """Custom type panSctpEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSctpEndReason_Type.__name__ = "OctetString"
_PanSctpEndReason_Object = MibScalar
panSctpEndReason = _PanSctpEndReason_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 716),
    _PanSctpEndReason_Type()
)
panSctpEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpEndReason.setStatus("current")
_PanSctpChunks_Type = Counter32
_PanSctpChunks_Object = MibScalar
panSctpChunks = _PanSctpChunks_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 717),
    _PanSctpChunks_Type()
)
panSctpChunks.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpChunks.setStatus("current")
_PanSctpPackets_Type = Counter32
_PanSctpPackets_Object = MibScalar
panSctpPackets = _PanSctpPackets_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 718),
    _PanSctpPackets_Type()
)
panSctpPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSctpPackets.setStatus("current")
_PanIpTagIp_Type = IpAddress
_PanIpTagIp_Object = MibScalar
panIpTagIp = _PanIpTagIp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 750),
    _PanIpTagIp_Type()
)
panIpTagIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagIp.setStatus("current")


class _PanIpTagName_Type(OctetString):
    """Custom type panIpTagName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanIpTagName_Type.__name__ = "OctetString"
_PanIpTagName_Object = MibScalar
panIpTagName = _PanIpTagName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 751),
    _PanIpTagName_Type()
)
panIpTagName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagName.setStatus("current")


class _PanIpTagEvent_Type(OctetString):
    """Custom type panIpTagEvent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanIpTagEvent_Type.__name__ = "OctetString"
_PanIpTagEvent_Object = MibScalar
panIpTagEvent = _PanIpTagEvent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 752),
    _PanIpTagEvent_Type()
)
panIpTagEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagEvent.setStatus("current")
_PanIpTagRepeatCount_Type = Counter32
_PanIpTagRepeatCount_Object = MibScalar
panIpTagRepeatCount = _PanIpTagRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 753),
    _PanIpTagRepeatCount_Type()
)
panIpTagRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagRepeatCount.setStatus("current")
_PanIpTagTimeout_Type = Counter32
_PanIpTagTimeout_Object = MibScalar
panIpTagTimeout = _PanIpTagTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 754),
    _PanIpTagTimeout_Type()
)
panIpTagTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagTimeout.setStatus("current")


class _PanIpTagDataSourceName_Type(OctetString):
    """Custom type panIpTagDataSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanIpTagDataSourceName_Type.__name__ = "OctetString"
_PanIpTagDataSourceName_Object = MibScalar
panIpTagDataSourceName = _PanIpTagDataSourceName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 755),
    _PanIpTagDataSourceName_Type()
)
panIpTagDataSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagDataSourceName.setStatus("current")


class _PanIpTagDataSourceType_Type(OctetString):
    """Custom type panIpTagDataSourceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanIpTagDataSourceType_Type.__name__ = "OctetString"
_PanIpTagDataSourceType_Object = MibScalar
panIpTagDataSourceType = _PanIpTagDataSourceType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 756),
    _PanIpTagDataSourceType_Type()
)
panIpTagDataSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagDataSourceType.setStatus("current")


class _PanIpTagDataSourceSubType_Type(OctetString):
    """Custom type panIpTagDataSourceSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanIpTagDataSourceSubType_Type.__name__ = "OctetString"
_PanIpTagDataSourceSubType_Object = MibScalar
panIpTagDataSourceSubType = _PanIpTagDataSourceSubType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 757),
    _PanIpTagDataSourceSubType_Type()
)
panIpTagDataSourceSubType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIpTagDataSourceSubType.setStatus("current")
_PanGlobalProtectStatus_Type = Integer32
_PanGlobalProtectStatus_Object = MibScalar
panGlobalProtectStatus = _PanGlobalProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 900),
    _PanGlobalProtectStatus_Type()
)
panGlobalProtectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectStatus.setStatus("current")


class _PanGlobalProtectStage_Type(OctetString):
    """Custom type panGlobalProtectStage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGlobalProtectStage_Type.__name__ = "OctetString"
_PanGlobalProtectStage_Object = MibScalar
panGlobalProtectStage = _PanGlobalProtectStage_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 901),
    _PanGlobalProtectStage_Type()
)
panGlobalProtectStage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectStage.setStatus("current")


class _PanGlobalProtectAuthMethod_Type(OctetString):
    """Custom type panGlobalProtectAuthMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGlobalProtectAuthMethod_Type.__name__ = "OctetString"
_PanGlobalProtectAuthMethod_Object = MibScalar
panGlobalProtectAuthMethod = _PanGlobalProtectAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 902),
    _PanGlobalProtectAuthMethod_Type()
)
panGlobalProtectAuthMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectAuthMethod.setStatus("current")


class _PanGlobalProtectTunnelType_Type(OctetString):
    """Custom type panGlobalProtectTunnelType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanGlobalProtectTunnelType_Type.__name__ = "OctetString"
_PanGlobalProtectTunnelType_Object = MibScalar
panGlobalProtectTunnelType = _PanGlobalProtectTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 903),
    _PanGlobalProtectTunnelType_Type()
)
panGlobalProtectTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectTunnelType.setStatus("current")


class _PanGlobalProtectPortal_Type(OctetString):
    """Custom type panGlobalProtectPortal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGlobalProtectPortal_Type.__name__ = "OctetString"
_PanGlobalProtectPortal_Object = MibScalar
panGlobalProtectPortal = _PanGlobalProtectPortal_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 904),
    _PanGlobalProtectPortal_Type()
)
panGlobalProtectPortal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectPortal.setStatus("current")


class _PanGlobalProtectSrcRegion_Type(OctetString):
    """Custom type panGlobalProtectSrcRegion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGlobalProtectSrcRegion_Type.__name__ = "OctetString"
_PanGlobalProtectSrcRegion_Object = MibScalar
panGlobalProtectSrcRegion = _PanGlobalProtectSrcRegion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 905),
    _PanGlobalProtectSrcRegion_Type()
)
panGlobalProtectSrcRegion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectSrcRegion.setStatus("current")
_PanGlobalProtectPublicIP_Type = IpAddress
_PanGlobalProtectPublicIP_Object = MibScalar
panGlobalProtectPublicIP = _PanGlobalProtectPublicIP_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 906),
    _PanGlobalProtectPublicIP_Type()
)
panGlobalProtectPublicIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectPublicIP.setStatus("current")
_PanGlobalProtectPublicIPv6_Type = IpAddress
_PanGlobalProtectPublicIPv6_Object = MibScalar
panGlobalProtectPublicIPv6 = _PanGlobalProtectPublicIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 907),
    _PanGlobalProtectPublicIPv6_Type()
)
panGlobalProtectPublicIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectPublicIPv6.setStatus("current")
_PanGlobalProtectPrivateIP_Type = IpAddress
_PanGlobalProtectPrivateIP_Object = MibScalar
panGlobalProtectPrivateIP = _PanGlobalProtectPrivateIP_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 908),
    _PanGlobalProtectPrivateIP_Type()
)
panGlobalProtectPrivateIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectPrivateIP.setStatus("current")
_PanGlobalProtectPrivateIPv6_Type = IpAddress
_PanGlobalProtectPrivateIPv6_Object = MibScalar
panGlobalProtectPrivateIPv6 = _PanGlobalProtectPrivateIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 909),
    _PanGlobalProtectPrivateIPv6_Type()
)
panGlobalProtectPrivateIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectPrivateIPv6.setStatus("current")
_PanGlobalProtectClientVersion_Type = Integer32
_PanGlobalProtectClientVersion_Object = MibScalar
panGlobalProtectClientVersion = _PanGlobalProtectClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 910),
    _PanGlobalProtectClientVersion_Type()
)
panGlobalProtectClientVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectClientVersion.setStatus("current")


class _PanGlobalProtectClientOSVersion_Type(OctetString):
    """Custom type panGlobalProtectClientOSVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanGlobalProtectClientOSVersion_Type.__name__ = "OctetString"
_PanGlobalProtectClientOSVersion_Object = MibScalar
panGlobalProtectClientOSVersion = _PanGlobalProtectClientOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 911),
    _PanGlobalProtectClientOSVersion_Type()
)
panGlobalProtectClientOSVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectClientOSVersion.setStatus("current")
_PanGlobalProtectLoginDuration_Type = Integer32
_PanGlobalProtectLoginDuration_Object = MibScalar
panGlobalProtectLoginDuration = _PanGlobalProtectLoginDuration_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 912),
    _PanGlobalProtectLoginDuration_Type()
)
panGlobalProtectLoginDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectLoginDuration.setStatus("current")


class _PanGlobalProtectConnectMethod_Type(OctetString):
    """Custom type panGlobalProtectConnectMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGlobalProtectConnectMethod_Type.__name__ = "OctetString"
_PanGlobalProtectConnectMethod_Object = MibScalar
panGlobalProtectConnectMethod = _PanGlobalProtectConnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 913),
    _PanGlobalProtectConnectMethod_Type()
)
panGlobalProtectConnectMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectConnectMethod.setStatus("current")


class _PanGlobalProtectReason_Type(OctetString):
    """Custom type panGlobalProtectReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanGlobalProtectReason_Type.__name__ = "OctetString"
_PanGlobalProtectReason_Object = MibScalar
panGlobalProtectReason = _PanGlobalProtectReason_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 914),
    _PanGlobalProtectReason_Type()
)
panGlobalProtectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectReason.setStatus("current")


class _PanGlobalProtectLocation_Type(OctetString):
    """Custom type panGlobalProtectLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanGlobalProtectLocation_Type.__name__ = "OctetString"
_PanGlobalProtectLocation_Object = MibScalar
panGlobalProtectLocation = _PanGlobalProtectLocation_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 915),
    _PanGlobalProtectLocation_Type()
)
panGlobalProtectLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectLocation.setStatus("current")
_PanGlobalProtectErrorCode_Type = Integer32
_PanGlobalProtectErrorCode_Object = MibScalar
panGlobalProtectErrorCode = _PanGlobalProtectErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 916),
    _PanGlobalProtectErrorCode_Type()
)
panGlobalProtectErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectErrorCode.setStatus("current")


class _PanGlobalProtectError_Type(OctetString):
    """Custom type panGlobalProtectError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanGlobalProtectError_Type.__name__ = "OctetString"
_PanGlobalProtectError_Object = MibScalar
panGlobalProtectError = _PanGlobalProtectError_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 917),
    _PanGlobalProtectError_Type()
)
panGlobalProtectError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panGlobalProtectError.setStatus("current")

# Managed Objects groups


# Notification objects

panConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2)
)
panConfigTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panHost"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panConfigCmd"),
        ("PAN-TRAPS", "panConfigAdmin"),
        ("PAN-TRAPS", "panConfigClient"),
        ("PAN-TRAPS", "panConfigResult"),
        ("PAN-TRAPS", "panConfigPath"))
)
if mibBuilder.loadTexts:
    panConfigTrap.setStatus(
        "current"
    )

panTrafficTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3)
)
panTrafficTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panSourceUUID"),
        ("PAN-TRAPS", "panDestinationUUID"),
        ("PAN-TRAPS", "panRuleUUID"),
        ("PAN-TRAPS", "panTunnel"),
        ("PAN-TRAPS", "panTrafficBytes"),
        ("PAN-TRAPS", "panTrafficPackets"),
        ("PAN-TRAPS", "panTrafficStartTime"),
        ("PAN-TRAPS", "panTrafficElapsed"),
        ("PAN-TRAPS", "panTrafficCategory"),
        ("PAN-TRAPS", "panTrafficSessionEndReason"),
        ("PAN-TRAPS", "panTrafficTunnelID"),
        ("PAN-TRAPS", "panTrafficImsi"),
        ("PAN-TRAPS", "panTrafficMonitorTag"),
        ("PAN-TRAPS", "panTrafficImei"),
        ("PAN-TRAPS", "panTrafficParentSessionId"),
        ("PAN-TRAPS", "panTrafficParentStartTime"))
)
if mibBuilder.loadTexts:
    panTrafficTrap.setStatus(
        "current"
    )

panThreatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4)
)
panThreatTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panSourceUUID"),
        ("PAN-TRAPS", "panDestinationUUID"),
        ("PAN-TRAPS", "panRuleUUID"),
        ("PAN-TRAPS", "panTunnel"),
        ("PAN-TRAPS", "panThreatId"),
        ("PAN-TRAPS", "panThreatCategory"),
        ("PAN-TRAPS", "panThreatContentType"),
        ("PAN-TRAPS", "panThreatSeverity"),
        ("PAN-TRAPS", "panThreatDirection"),
        ("PAN-TRAPS", "panMiscellaneous"),
        ("PAN-TRAPS", "panPcapId"),
        ("PAN-TRAPS", "panFileDigest"),
        ("PAN-TRAPS", "panCloud"),
        ("PAN-TRAPS", "panUrlIndex"),
        ("PAN-TRAPS", "panUserAgent"),
        ("PAN-TRAPS", "panXff"),
        ("PAN-TRAPS", "panReferer"),
        ("PAN-TRAPS", "panSender"),
        ("PAN-TRAPS", "panSubject"),
        ("PAN-TRAPS", "panRecipient"),
        ("PAN-TRAPS", "panFileType"),
        ("PAN-TRAPS", "panReportId"),
        ("PAN-TRAPS", "panHttpMethod"),
        ("PAN-TRAPS", "panThreatTunnelID"),
        ("PAN-TRAPS", "panThreatImsi"),
        ("PAN-TRAPS", "panThreatMonitorTag"),
        ("PAN-TRAPS", "panThreatImei"),
        ("PAN-TRAPS", "panThreatParentSessionId"),
        ("PAN-TRAPS", "panThreatParentStartTime"),
        ("PAN-TRAPS", "panThrCategory"))
)
if mibBuilder.loadTexts:
    panThreatTrap.setStatus(
        "current"
    )

panHipMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 5)
)
panHipMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panHipSourceUser"),
        ("PAN-TRAPS", "panHipMachineName"),
        ("PAN-TRAPS", "panHipSource"),
        ("PAN-TRAPS", "panHipMatch"),
        ("PAN-TRAPS", "panHipMatchType"),
        ("PAN-TRAPS", "panHipRepeatCount"),
        ("PAN-TRAPS", "panHipOS"),
        ("PAN-TRAPS", "panHipSourceIPv6"))
)
if mibBuilder.loadTexts:
    panHipMatchTrap.setStatus(
        "current"
    )

panGtpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 6)
)
panGtpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panTunnel"),
        ("PAN-TRAPS", "panGtpParentSessionId"),
        ("PAN-TRAPS", "panGtpParentStartTime"),
        ("PAN-TRAPS", "panGtpMsisdn"),
        ("PAN-TRAPS", "panGtpApn"),
        ("PAN-TRAPS", "panGtpRat"),
        ("PAN-TRAPS", "panGtpMsgType"),
        ("PAN-TRAPS", "panGtpTunnelID"),
        ("PAN-TRAPS", "panGtpImsi"),
        ("PAN-TRAPS", "panGtpMonitorTag"),
        ("PAN-TRAPS", "panGtpImei"),
        ("PAN-TRAPS", "panGtpInterface"),
        ("PAN-TRAPS", "panGtpCauseCode"),
        ("PAN-TRAPS", "panGtpEventType"),
        ("PAN-TRAPS", "panGtpSeverity"),
        ("PAN-TRAPS", "panGtpMcc"),
        ("PAN-TRAPS", "panGtpMnc"),
        ("PAN-TRAPS", "panGtpEventCode"),
        ("PAN-TRAPS", "panGtpBytes"),
        ("PAN-TRAPS", "panGtpPackets"),
        ("PAN-TRAPS", "panGtpMaxEncap"),
        ("PAN-TRAPS", "panGtpUnknownProto"),
        ("PAN-TRAPS", "panGtpStrictCheck"),
        ("PAN-TRAPS", "panGtpTunnelFragment"),
        ("PAN-TRAPS", "panGtpSessionsCreated"),
        ("PAN-TRAPS", "panGtpSessionsClosed"),
        ("PAN-TRAPS", "panGtpSessionEndReason"),
        ("PAN-TRAPS", "panGtpActionSource"),
        ("PAN-TRAPS", "panGtpStartTime"),
        ("PAN-TRAPS", "panGtpElapsed"),
        ("PAN-TRAPS", "panGtpTCIRule"),
        ("PAN-TRAPS", "panGtpRemoteUserIp"),
        ("PAN-TRAPS", "panGtpRemoteUserId"),
        ("PAN-TRAPS", "panRuleUUID"))
)
if mibBuilder.loadTexts:
    panGtpTrap.setStatus(
        "current"
    )

panUseridTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 7)
)
panUseridTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panUseridUser"),
        ("PAN-TRAPS", "panUseridDataSourceName"),
        ("PAN-TRAPS", "panUseridEventID"),
        ("PAN-TRAPS", "panUseridRepeatCount"),
        ("PAN-TRAPS", "panUseridTimeout"),
        ("PAN-TRAPS", "panUseridBeginport"),
        ("PAN-TRAPS", "panUseridEndport"),
        ("PAN-TRAPS", "panUseridDataSource"),
        ("PAN-TRAPS", "panUseridDataSourceType"),
        ("PAN-TRAPS", "panUseridFactorType"),
        ("PAN-TRAPS", "panUseridFactorTime"),
        ("PAN-TRAPS", "panUseridFactorNo"))
)
if mibBuilder.loadTexts:
    panUseridTrap.setStatus(
        "current"
    )

panAuthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 8)
)
panAuthTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panAuthUser"),
        ("PAN-TRAPS", "panAuthNormalizeUser"),
        ("PAN-TRAPS", "panAuthObject"),
        ("PAN-TRAPS", "panAuthPolicy"),
        ("PAN-TRAPS", "panAuthRepeatCount"),
        ("PAN-TRAPS", "panAuthID"),
        ("PAN-TRAPS", "panAuthVendor"),
        ("PAN-TRAPS", "panAuthLogForwardingProfile"),
        ("PAN-TRAPS", "panAuthClientType"),
        ("PAN-TRAPS", "panAuthDescription"),
        ("PAN-TRAPS", "panAuthServerProfile"),
        ("PAN-TRAPS", "panAuthEvent"),
        ("PAN-TRAPS", "panAuthFactorNo"),
        ("PAN-TRAPS", "panAuthProto"))
)
if mibBuilder.loadTexts:
    panAuthTrap.setStatus(
        "current"
    )

panSctpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 9)
)
panSctpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panSctpAssocId"),
        ("PAN-TRAPS", "panSctpPpid"),
        ("PAN-TRAPS", "panSctpSeverity"),
        ("PAN-TRAPS", "panSctpChunkType"),
        ("PAN-TRAPS", "panSctpEventType"),
        ("PAN-TRAPS", "panSctpEventCode"),
        ("PAN-TRAPS", "panSctpVerifTag1"),
        ("PAN-TRAPS", "panSctpVerifTag2"),
        ("PAN-TRAPS", "panSctpCauseCode"),
        ("PAN-TRAPS", "panSctpDiamAppId"),
        ("PAN-TRAPS", "panSctpDiamCmdCode"),
        ("PAN-TRAPS", "panSctpDiamAvpCode"),
        ("PAN-TRAPS", "panSctpStreamId"),
        ("PAN-TRAPS", "panSctpOpCode"),
        ("PAN-TRAPS", "panSctpCallingSSN"),
        ("PAN-TRAPS", "panSctpCallingGT"),
        ("PAN-TRAPS", "panSctpEndReason"),
        ("PAN-TRAPS", "panSctpChunks"),
        ("PAN-TRAPS", "panSctpPackets"),
        ("PAN-TRAPS", "panRuleUUID"))
)
if mibBuilder.loadTexts:
    panSctpTrap.setStatus(
        "current"
    )

panCorrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 10)
)
panCorrTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panCorrSeverity"),
        ("PAN-TRAPS", "panCorrDG1"),
        ("PAN-TRAPS", "panCorrDG2"),
        ("PAN-TRAPS", "panCorrDG3"),
        ("PAN-TRAPS", "panCorrDG4"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panCorrObjName"),
        ("PAN-TRAPS", "panCorrObjID"),
        ("PAN-TRAPS", "panCorrEvidence"))
)
if mibBuilder.loadTexts:
    panCorrTrap.setStatus(
        "current"
    )

panIpTagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 11)
)
panIpTagTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panIpTagIp"),
        ("PAN-TRAPS", "panIpTagName"),
        ("PAN-TRAPS", "panIpTagEvent"),
        ("PAN-TRAPS", "panIpTagRepeatCount"),
        ("PAN-TRAPS", "panIpTagTimeout"),
        ("PAN-TRAPS", "panIpTagDataSourceName"),
        ("PAN-TRAPS", "panIpTagDataSourceType"),
        ("PAN-TRAPS", "panIpTagDataSourceSubType"))
)
if mibBuilder.loadTexts:
    panIpTagTrap.setStatus(
        "current"
    )

panGlobalprotectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 12)
)
panGlobalprotectTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panGlobalProtectStatus"),
        ("PAN-TRAPS", "panGlobalProtectStage"),
        ("PAN-TRAPS", "panGlobalProtectAuthMethod"),
        ("PAN-TRAPS", "panGlobalProtectTunnelType"),
        ("PAN-TRAPS", "panGlobalProtectPortal"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panGlobalProtectSrcRegion"),
        ("PAN-TRAPS", "panHipMachineName"),
        ("PAN-TRAPS", "panGlobalProtectPublicIP"),
        ("PAN-TRAPS", "panGlobalProtectPublicIPv6"),
        ("PAN-TRAPS", "panGlobalProtectPrivateIP"),
        ("PAN-TRAPS", "panGlobalProtectPrivateIPv6"),
        ("PAN-TRAPS", "panHostId"),
        ("PAN-TRAPS", "panSerialNo"),
        ("PAN-TRAPS", "panGlobalProtectClientVersion"),
        ("PAN-TRAPS", "panGlobalProtectClientOSVersion"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panGlobalProtectLoginDuration"),
        ("PAN-TRAPS", "panGlobalProtectConnectMethod"),
        ("PAN-TRAPS", "panGlobalProtectReason"),
        ("PAN-TRAPS", "panGlobalProtectLocation"),
        ("PAN-TRAPS", "panGlobalProtectErrorCode"),
        ("PAN-TRAPS", "panGlobalProtectError"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectTrap.setStatus(
        "current"
    )

panCryptoCertExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 100)
)
panCryptoCertExpiryTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoCertExpiryTrap.setStatus(
        "current"
    )

panCryptoMkeyExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 101)
)
panCryptoMkeyExpiryTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoMkeyExpiryTrap.setStatus(
        "current"
    )

panCryptoMkeyExpiryReminderTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 102)
)
panCryptoMkeyExpiryReminderTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoMkeyExpiryReminderTrap.setStatus(
        "current"
    )

panCryptoHSMStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 103)
)
panCryptoHSMStateChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoHSMStateChangeTrap.setStatus(
        "current"
    )

panCryptoPrivateKeyExportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 104)
)
panCryptoPrivateKeyExportTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoPrivateKeyExportTrap.setStatus(
        "current"
    )

panCryptoDeployMkeyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 105)
)
panCryptoDeployMkeyChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoDeployMkeyChangeTrap.setStatus(
        "current"
    )

panCryptoMkeyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 106)
)
panCryptoMkeyChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoMkeyChangeTrap.setStatus(
        "current"
    )

panDHCPLeaseStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 200)
)
panDHCPLeaseStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPLeaseStartTrap.setStatus(
        "current"
    )

panDHCPLeaseEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 201)
)
panDHCPLeaseEndTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPLeaseEndTrap.setStatus(
        "current"
    )

panDHCPServerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 202)
)
panDHCPServerOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerOnTrap.setStatus(
        "current"
    )

panDHCPServerAutoProbeOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 203)
)
panDHCPServerAutoProbeOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerAutoProbeOnTrap.setStatus(
        "current"
    )

panDHCPServerAutoProbeOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 204)
)
panDHCPServerAutoProbeOffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerAutoProbeOffTrap.setStatus(
        "current"
    )

panDHCPServerNoFreeIpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 205)
)
panDHCPServerNoFreeIpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerNoFreeIpTrap.setStatus(
        "current"
    )

panDHCPIpAlreadyInUseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 206)
)
panDHCPIpAlreadyInUseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIpAlreadyInUseTrap.setStatus(
        "current"
    )

panDHCPRelayOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 207)
)
panDHCPRelayOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelayOnTrap.setStatus(
        "current"
    )

panDHCPRelayOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 208)
)
panDHCPRelayOffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelayOffTrap.setStatus(
        "current"
    )

panDHCPRelay6OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 209)
)
panDHCPRelay6OnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelay6OnTrap.setStatus(
        "current"
    )

panDHCPRelay6OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 210)
)
panDHCPRelay6OffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelay6OffTrap.setStatus(
        "current"
    )

panDHCPIfUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 211)
)
panDHCPIfUpdateFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfUpdateFailTrap.setStatus(
        "current"
    )

panDHCPIfUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 212)
)
panDHCPIfUpdateOkTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfUpdateOkTrap.setStatus(
        "current"
    )

panDHCPIfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 213)
)
panDHCPIfClearTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfClearTrap.setStatus(
        "current"
    )

panDHCPIfRenewTriggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 214)
)
panDHCPIfRenewTriggerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfRenewTriggerTrap.setStatus(
        "current"
    )

panDHCPIfReleaseTriggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 215)
)
panDHCPIfReleaseTriggerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfReleaseTriggerTrap.setStatus(
        "current"
    )

panDHCPIfRcvNakTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 216)
)
panDHCPIfRcvNakTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfRcvNakTrap.setStatus(
        "current"
    )

panDHCPIfInheritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 217)
)
panDHCPIfInheritTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfInheritTrap.setStatus(
        "current"
    )

panDHCPIfDuplicateIpIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 218)
)
panDHCPIfDuplicateIpIntfTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfDuplicateIpIntfTrap.setStatus(
        "current"
    )

panDHCPIfDuplicateIpRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 219)
)
panDHCPIfDuplicateIpRemoteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfDuplicateIpRemoteTrap.setStatus(
        "current"
    )

panDNSProxyCacheClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 300)
)
panDNSProxyCacheClearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyCacheClearedTrap.setStatus(
        "current"
    )

panDNSProxyResolveFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 301)
)
panDNSProxyResolveFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyResolveFailTrap.setStatus(
        "current"
    )

panDNSProxyObjectEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 302)
)
panDNSProxyObjectEnableTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyObjectEnableTrap.setStatus(
        "current"
    )

panDNSProxyIfAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 303)
)
panDNSProxyIfAddTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfAddTrap.setStatus(
        "current"
    )

panDNSProxyIfDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 304)
)
panDNSProxyIfDelTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfDelTrap.setStatus(
        "current"
    )

panDNSProxyIfInheritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 305)
)
panDNSProxyIfInheritTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfInheritTrap.setStatus(
        "current"
    )

panDOSDosRuleChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 500)
)
panDOSDosRuleChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDOSDosRuleChangedTrap.setStatus(
        "current"
    )

panGeneralGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 600)
)
panGeneralGeneralTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralGeneralTrap.setStatus(
        "current"
    )

panGeneralSystemStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 601)
)
panGeneralSystemStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralSystemStartTrap.setStatus(
        "current"
    )

panGeneralSystemShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 602)
)
panGeneralSystemShutdownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralSystemShutdownTrap.setStatus(
        "current"
    )

panGeneralAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 603)
)
panGeneralAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthFailTrap.setStatus(
        "current"
    )

panGeneralAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 604)
)
panGeneralAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthSuccessTrap.setStatus(
        "current"
    )

panGeneralTacLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 605)
)
panGeneralTacLoginTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralTacLoginTrap.setStatus(
        "current"
    )

panGeneralAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 606)
)
panGeneralAuthServerDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthServerDownTrap.setStatus(
        "current"
    )

panGeneralAdminDiscardTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 607)
)
panGeneralAdminDiscardTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAdminDiscardTrap.setStatus(
        "current"
    )

panGeneralBootstrapFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 608)
)
panGeneralBootstrapFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralBootstrapFailureTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRegistSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 700)
)
panGlobalprotectgatewayRegistSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRegistSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRegistFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 701)
)
panGlobalprotectgatewayRegistFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRegistFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayLogoutSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 702)
)
panGlobalprotectgatewayLogoutSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayLogoutSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayLogoutFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 703)
)
panGlobalprotectgatewayLogoutFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayLogoutFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 704)
)
panGlobalProtectGatewayConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 705)
)
panGlobalProtectGatewayConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 706)
)
panGlobalProtectGatewayConfigReleaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigReleaseTrap.setStatus(
        "current"
    )

panGlobalProtectGatewaySwitchSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 707)
)
panGlobalProtectGatewaySwitchSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewaySwitchSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewaySwitchFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 708)
)
panGlobalProtectGatewaySwitchFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewaySwitchFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 709)
)
panGlobalProtectGatewayAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAuthSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 710)
)
panGlobalProtectGatewayAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAuthFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAgentMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 711)
)
panGlobalProtectGatewayAgentMsgTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAgentMsgTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayInvalidLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 712)
)
panGlobalProtectGatewayInvalidLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayInvalidLicenseTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayInheritanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 713)
)
panGlobalProtectGatewayInheritanceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayInheritanceTrap.setStatus(
        "current"
    )

panGlobalProtectPortalConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 714)
)
panGlobalProtectPortalConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalConfigSuccTrap.setStatus(
        "current"
    )

panGlobalProtectPortalConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 715)
)
panGlobalProtectPortalConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalConfigFailTrap.setStatus(
        "current"
    )

panGlobalProtectPortalAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 716)
)
panGlobalProtectPortalAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalAuthSuccTrap.setStatus(
        "current"
    )

panGlobalProtectPortalAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 717)
)
panGlobalProtectPortalAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalAuthFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewaySatauthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 718)
)
panGlobalprotectgatewaySatauthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewaySatauthSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewaySatauthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 719)
)
panGlobalprotectgatewaySatauthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewaySatauthFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRouteAddFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 720)
)
panGlobalprotectgatewayRouteAddFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRouteAddFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRouteResetFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 721)
)
panGlobalprotectgatewayRouteResetFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRouteResetFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 722)
)
panGlobalprotectgatewayTunUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunUpTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 723)
)
panGlobalprotectgatewayTunDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunDownTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayDupSubnetsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 724)
)
panGlobalprotectgatewayDupSubnetsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayDupSubnetsTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayDeniedRoutesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 725)
)
panGlobalprotectgatewayDeniedRoutesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayDeniedRoutesTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunMonDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 726)
)
panGlobalprotectgatewayTunMonDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunMonDownTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunMonUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 727)
)
panGlobalprotectgatewayTunMonUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunMonUpTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatconfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 728)
)
panGlobalprotectportalSatconfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatconfigSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatconfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 729)
)
panGlobalprotectportalSatconfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatconfigFailTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatauthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 730)
)
panGlobalprotectportalSatauthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatauthSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatauthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 731)
)
panGlobalprotectportalSatauthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatauthFailTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatcertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 732)
)
panGlobalprotectportalSatcertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatcertSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatcertFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 733)
)
panGlobalprotectportalSatcertFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatcertFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunHardlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 734)
)
panGlobalprotectgatewayTunHardlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunHardlifetimeExpiredTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunDpInstallErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 735)
)
panGlobalprotectgatewayTunDpInstallErrTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunDpInstallErrTrap.setStatus(
        "current"
    )

panGlobalprotectportalGenportalcookieSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 736)
)
panGlobalprotectportalGenportalcookieSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalGenportalcookieSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalGenportalcookieFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 737)
)
panGlobalprotectportalGenportalcookieFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalGenportalcookieFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 738)
)
panGlobalprotectgatewayFramedIpSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 739)
)
panGlobalprotectgatewayFramedIpFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayGencookieSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 740)
)
panGlobalprotectgatewayGencookieSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayGencookieSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayGencookieFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 741)
)
panGlobalprotectgatewayGencookieFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayGencookieFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpv6SuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 742)
)
panGlobalprotectgatewayFramedIpv6SuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpv6SuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpv6FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 743)
)
panGlobalprotectgatewayFramedIpv6FailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpv6FailTrap.setStatus(
        "current"
    )

panGlobalprotectportalLogoutSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 744)
)
panGlobalprotectportalLogoutSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalLogoutSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalLogoutFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 745)
)
panGlobalprotectportalLogoutFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalLogoutFailTrap.setStatus(
        "current"
    )

panHAPreemptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 800)
)
panHAPreemptTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPreemptTrap.setStatus(
        "current"
    )

panHAStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 801)
)
panHAStateChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAStateChangeTrap.setStatus(
        "current"
    )

panHAStateOverrideTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 802)
)
panHAStateOverrideTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAStateOverrideTrap.setStatus(
        "current"
    )

panHADataplaneDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 803)
)
panHADataplaneDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHADataplaneDownTrap.setStatus(
        "current"
    )

panHAPolicyPushFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 804)
)
panHAPolicyPushFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPolicyPushFailTrap.setStatus(
        "current"
    )

panHAHa1LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 805)
)
panHAHa1LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa1LinkChangeTrap.setStatus(
        "current"
    )

panHAHa2LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 806)
)
panHAHa2LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa2LinkChangeTrap.setStatus(
        "current"
    )

panHAConnectChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 807)
)
panHAConnectChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConnectChangeTrap.setStatus(
        "current"
    )

panHAPathMonitorDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 808)
)
panHAPathMonitorDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPathMonitorDownTrap.setStatus(
        "current"
    )

panHALinkMonitorDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 809)
)
panHALinkMonitorDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHALinkMonitorDownTrap.setStatus(
        "current"
    )

panHAHa3LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 810)
)
panHAHa3LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa3LinkChangeTrap.setStatus(
        "current"
    )

panHAPathMonitorUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 811)
)
panHAPathMonitorUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPathMonitorUpTrap.setStatus(
        "current"
    )

panHALinkMonitorUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 812)
)
panHALinkMonitorUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHALinkMonitorUpTrap.setStatus(
        "current"
    )

panHAPeerSyncFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 813)
)
panHAPeerSyncFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerSyncFailureTrap.setStatus(
        "current"
    )

panHAConfigFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 814)
)
panHAConfigFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConfigFailureTrap.setStatus(
        "current"
    )

panHAConfigNotSynchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 815)
)
panHAConfigNotSynchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConfigNotSynchTrap.setStatus(
        "current"
    )

panHAPeerErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 816)
)
panHAPeerErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerErrorTrap.setStatus(
        "current"
    )

panHAPre13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 817)
)
panHAPre13Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPre13Trap.setStatus(
        "current"
    )

panHAPre20Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 818)
)
panHAPre20Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPre20Trap.setStatus(
        "current"
    )

panHAPeerVersionMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 819)
)
panHAPeerVersionMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionMatchTrap.setStatus(
        "current"
    )

panHAPeerVersionSupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 820)
)
panHAPeerVersionSupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionSupportedTrap.setStatus(
        "current"
    )

panHAPeerVersionUnsupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 821)
)
panHAPeerVersionUnsupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionUnsupportedTrap.setStatus(
        "current"
    )

panHAPeerVersionDegradedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 822)
)
panHAPeerVersionDegradedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionDegradedTrap.setStatus(
        "current"
    )

panHAPeerCompatMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 823)
)
panHAPeerCompatMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatMismatchTrap.setStatus(
        "current"
    )

panHAPeerCompatMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 824)
)
panHAPeerCompatMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatMatchTrap.setStatus(
        "current"
    )

panHAPeerCompatFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 825)
)
panHAPeerCompatFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatFailTrap.setStatus(
        "current"
    )

panHAPeerSplitBrainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 826)
)
panHAPeerSplitBrainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerSplitBrainTrap.setStatus(
        "current"
    )

panHASplitBrainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 827)
)
panHASplitBrainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASplitBrainTrap.setStatus(
        "current"
    )

panHAPreemptLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 828)
)
panHAPreemptLoopTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPreemptLoopTrap.setStatus(
        "current"
    )

panHANonFunctionalLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 829)
)
panHANonFunctionalLoopTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHANonFunctionalLoopTrap.setStatus(
        "current"
    )

panHAPeerShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 830)
)
panHAPeerShutdownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerShutdownTrap.setStatus(
        "current"
    )

panHANfsPanlogsFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 831)
)
panHANfsPanlogsFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHANfsPanlogsFailTrap.setStatus(
        "current"
    )

panHAInternalHaErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 832)
)
panHAInternalHaErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAInternalHaErrorTrap.setStatus(
        "current"
    )

panHASystemFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 833)
)
panHASystemFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASystemFailureTrap.setStatus(
        "current"
    )

panHAHa2KeepAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 834)
)
panHAHa2KeepAliveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa2KeepAliveTrap.setStatus(
        "current"
    )

panHASlotFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 835)
)
panHASlotFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotFailureTrap.setStatus(
        "current"
    )

panHASlotMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 836)
)
panHASlotMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotMismatchTrap.setStatus(
        "current"
    )

panHASlotControlFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 837)
)
panHASlotControlFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotControlFailureTrap.setStatus(
        "current"
    )

panHASlotControlEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 838)
)
panHASlotControlEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotControlEventTrap.setStatus(
        "current"
    )

panHASessionSynchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 839)
)
panHASessionSynchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASessionSynchTrap.setStatus(
        "current"
    )

panHAVmAwsInterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 840)
)
panHAVmAwsInterfaceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAVmAwsInterfaceTrap.setStatus(
        "current"
    )

panHWDiskErrorsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 900)
)
panHWDiskErrorsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWDiskErrorsTrap.setStatus(
        "current"
    )

panHWSlotUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 901)
)
panHWSlotUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotUpTrap.setStatus(
        "current"
    )

panHWInsufficientPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 902)
)
panHWInsufficientPowerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWInsufficientPowerTrap.setStatus(
        "current"
    )

panHWSlotUnsupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 903)
)
panHWSlotUnsupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotUnsupportedTrap.setStatus(
        "current"
    )

panHWSlotStartingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 904)
)
panHWSlotStartingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotStartingTrap.setStatus(
        "current"
    )

panHWSlotStoppingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 905)
)
panHWSlotStoppingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotStoppingTrap.setStatus(
        "current"
    )

panHWSlotFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 906)
)
panHWSlotFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotFailureTrap.setStatus(
        "current"
    )

panHWSlotPoweroffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 907)
)
panHWSlotPoweroffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotPoweroffTrap.setStatus(
        "current"
    )

panHWSlotAdminpoweroffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 908)
)
panHWSlotAdminpoweroffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotAdminpoweroffTrap.setStatus(
        "current"
    )

panHWSlotInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 909)
)
panHWSlotInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotInsertedTrap.setStatus(
        "current"
    )

panHWSlotRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 910)
)
panHWSlotRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotRemovedTrap.setStatus(
        "current"
    )

panHWPsInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 911)
)
panHWPsInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsInsertedTrap.setStatus(
        "current"
    )

panHWPsRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 912)
)
panHWPsRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsRemovedTrap.setStatus(
        "current"
    )

panHWPsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 913)
)
panHWPsFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsFailureTrap.setStatus(
        "current"
    )

panHWFanInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 914)
)
panHWFanInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanInsertedTrap.setStatus(
        "current"
    )

panHWFanRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 915)
)
panHWFanRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanRemovedTrap.setStatus(
        "current"
    )

panHWFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 916)
)
panHWFanFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanFailureTrap.setStatus(
        "current"
    )

panHWBootstrapImageErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 917)
)
panHWBootstrapImageErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapImageErrorTrap.setStatus(
        "current"
    )

panHWBootstrapConfigNotFoundTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 918)
)
panHWBootstrapConfigNotFoundTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapConfigNotFoundTrap.setStatus(
        "current"
    )

panHWBadParamsBootstrapConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 919)
)
panHWBadParamsBootstrapConfigTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBadParamsBootstrapConfigTrap.setStatus(
        "current"
    )

panHWMediaSanityFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 920)
)
panHWMediaSanityFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWMediaSanityFailureTrap.setStatus(
        "current"
    )

panHWUsbMediaPrepSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 921)
)
panHWUsbMediaPrepSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWUsbMediaPrepSuccessTrap.setStatus(
        "current"
    )

panHWBootstrapSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 922)
)
panHWBootstrapSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapSuccessTrap.setStatus(
        "current"
    )

panHWBootstrapLicenseFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 923)
)
panHWBootstrapLicenseFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapLicenseFailureTrap.setStatus(
        "current"
    )

panHWBootstrapContentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 924)
)
panHWBootstrapContentFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapContentFailureTrap.setStatus(
        "current"
    )

panHWBootstrapMediaDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 925)
)
panHWBootstrapMediaDetectTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapMediaDetectTrap.setStatus(
        "current"
    )

panHWBootstrapMediaSanityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 926)
)
panHWBootstrapMediaSanityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapMediaSanityTrap.setStatus(
        "current"
    )

panHWBootstrapImageUpgradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 927)
)
panHWBootstrapImageUpgradeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapImageUpgradeTrap.setStatus(
        "current"
    )

panHWBootstrapOpCmdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 928)
)
panHWBootstrapOpCmdTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWBootstrapOpCmdTrap.setStatus(
        "current"
    )

panNTDPRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1000)
)
panNTDPRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPRestartTrap.setStatus(
        "current"
    )

panNTDPTimeLearnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1001)
)
panNTDPTimeLearnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPTimeLearnTrap.setStatus(
        "current"
    )

panNTDPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1002)
)
panNTDPSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPSyncTrap.setStatus(
        "current"
    )

panNTDPAuthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1003)
)
panNTDPAuthTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPAuthTrap.setStatus(
        "current"
    )

panPBFNhUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1100)
)
panPBFNhUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPBFNhUpTrap.setStatus(
        "current"
    )

panPBFNhDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1101)
)
panPBFNhDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPBFNhDownTrap.setStatus(
        "current"
    )

panPORTLinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1200)
)
panPORTLinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTLinkChangeTrap.setStatus(
        "current"
    )

panPORTNonqualSfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1201)
)
panPORTNonqualSfpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualSfpTrap.setStatus(
        "current"
    )

panPORTNonqualSfpPlusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1202)
)
panPORTNonqualSfpPlusTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualSfpPlusTrap.setStatus(
        "current"
    )

panPORTNonqualXfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1203)
)
panPORTNonqualXfpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualXfpTrap.setStatus(
        "current"
    )

panPORTNonsuppForcedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1204)
)
panPORTNonsuppForcedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonsuppForcedTrap.setStatus(
        "current"
    )

panPORTInvalidModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1205)
)
panPORTInvalidModuleTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTInvalidModuleTrap.setStatus(
        "current"
    )

panPORTSdwanLinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1206)
)
panPORTSdwanLinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTSdwanLinkChangeTrap.setStatus(
        "current"
    )

panPPPOEInitiateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1300)
)
panPPPOEInitiateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEInitiateTrap.setStatus(
        "current"
    )

panPPPOEConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1301)
)
panPPPOEConnectTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEConnectTrap.setStatus(
        "current"
    )

panPPPOEConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1302)
)
panPPPOEConnectFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEConnectFailTrap.setStatus(
        "current"
    )

panPPPOETerminateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1303)
)
panPPPOETerminateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOETerminateTrap.setStatus(
        "current"
    )

panPPPOEIfUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1304)
)
panPPPOEIfUpdateFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEIfUpdateFailTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1400)
)
panRASRasmgrConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1SuccessTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1401)
)
panRASRasmgrConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1FailedTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1402)
)
panRASRasmgrConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1AbortTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1403)
)
panRASRasmgrConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP2SuccessTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1404)
)
panRASRasmgrConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP2FailedTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1405)
)
panRASRasmgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonStartTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1406)
)
panRASRasmgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonExitTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1407)
)
panRASRasmgrDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonInitTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1408)
)
panRASRasmgrFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncStartTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1409)
)
panRASRasmgrFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1410)
)
panRASRasmgrFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1411)
)
panRASRasmgrHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncStartTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1412)
)
panRASRasmgrHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncAbortTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1413)
)
panRASRasmgrHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncDoneTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1500)
)
panROUTINGRoutedConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1SuccessTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1501)
)
panROUTINGRoutedConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1FailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1502)
)
panROUTINGRoutedConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1AbortTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1503)
)
panROUTINGRoutedConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP2SuccessTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1504)
)
panROUTINGRoutedConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP2FailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1505)
)
panROUTINGRoutedDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonStartTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1506)
)
panROUTINGRoutedDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonExitTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1507)
)
panROUTINGRoutedDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonInitTrap.setStatus(
        "current"
    )

panROUTINGRoutedFibSyncPeerBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1508)
)
panROUTINGRoutedFibSyncPeerBackupTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedFibSyncPeerBackupTrap.setStatus(
        "current"
    )

panROUTINGRoutedFibSyncSelfMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1509)
)
panROUTINGRoutedFibSyncSelfMasterTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedFibSyncSelfMasterTrap.setStatus(
        "current"
    )

panROUTINGRoutedRTMBadRouteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1510)
)
panROUTINGRoutedRTMBadRouteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRTMBadRouteTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFLSAChksumFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1511)
)
panROUTINGRoutedOSPFLSAChksumFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFLSAChksumFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFLSAChksumInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1512)
)
panROUTINGRoutedOSPFLSAChksumInvalidTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFLSAChksumInvalidTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFAuthtypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1513)
)
panROUTINGRoutedOSPFAuthtypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFAuthtypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFPasswordBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1514)
)
panROUTINGRoutedOSPFPasswordBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFPasswordBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFChksumBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1515)
)
panROUTINGRoutedOSPFChksumBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFChksumBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFSequenceBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1516)
)
panROUTINGRoutedOSPFSequenceBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFSequenceBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFMd5chksumBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1517)
)
panROUTINGRoutedOSPFMd5chksumBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFMd5chksumBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFMd5lengthBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1518)
)
panROUTINGRoutedOSPFMd5lengthBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFMd5lengthBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloHelloIntvalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1519)
)
panROUTINGRoutedOSPFHelloHelloIntvalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloHelloIntvalBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloDeadIntvalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1520)
)
panROUTINGRoutedOSPFHelloDeadIntvalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloDeadIntvalBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloNetmaskBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1521)
)
panROUTINGRoutedOSPFHelloNetmaskBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloNetmaskBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloAreaTypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1522)
)
panROUTINGRoutedOSPFHelloAreaTypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloAreaTypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighbor2dirTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1523)
)
panROUTINGRoutedOSPFNeighbor2dirTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighbor2dirTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighborFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1524)
)
panROUTINGRoutedOSPFNeighborFullTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighborFullTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighborDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1525)
)
panROUTINGRoutedOSPFNeighborDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighborDownTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPPeerAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1526)
)
panROUTINGRoutedRIPPeerAddTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPPeerAddTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPPeerDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1527)
)
panROUTINGRoutedRIPPeerDelTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPPeerDelTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPAuthtypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1528)
)
panROUTINGRoutedRIPAuthtypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPAuthtypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1529)
)
panROUTINGRoutedRIPAuthFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPAuthFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPMd5lengthBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1530)
)
panROUTINGRoutedRIPMd5lengthBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPMd5lengthBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerEnterEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1531)
)
panROUTINGRoutedBGPPeerEnterEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerEnterEstablishedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerLeftEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1532)
)
panROUTINGRoutedBGPPeerLeftEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerLeftEstablishedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1533)
)
panROUTINGRoutedBGPPeerFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerRestartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1534)
)
panROUTINGRoutedBGPPeerRestartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerRestartedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerRestartFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1535)
)
panROUTINGRoutedBGPPeerRestartFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerRestartFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPRefreshSentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1536)
)
panROUTINGRoutedBGPRefreshSentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPRefreshSentTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPRibinRecalcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1537)
)
panROUTINGRoutedBGPRibinRecalcTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPRibinRecalcTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMInterfaceStateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1538)
)
panROUTINGRoutedPIMInterfaceStateChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMInterfaceStateChangedTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNewDrElectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1539)
)
panROUTINGRoutedPIMNewDrElectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNewDrElectedTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNeighborDiscoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1540)
)
panROUTINGRoutedPIMNeighborDiscoveredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNeighborDiscoveredTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNeighborDisappearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1541)
)
panROUTINGRoutedPIMNeighborDisappearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNeighborDisappearedTrap.setStatus(
        "current"
    )

panROUTINGRoutedIGMPWrongVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1542)
)
panROUTINGRoutedIGMPWrongVersionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedIGMPWrongVersionTrap.setStatus(
        "current"
    )

panROUTINGRoutedGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1543)
)
panROUTINGRoutedGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedGenericEventTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStartGracefulRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1544)
)
panROUTINGRoutedOSPFStartGracefulRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStartGracefulRestartTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStoppedGracefulRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1545)
)
panROUTINGRoutedOSPFStoppedGracefulRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStoppedGracefulRestartTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStartHelperNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1546)
)
panROUTINGRoutedOSPFStartHelperNodeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStartHelperNodeTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStopHelperModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1547)
)
panROUTINGRoutedOSPFStopHelperModeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStopHelperModeTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNotHelpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1548)
)
panROUTINGRoutedOSPFNotHelpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNotHelpTrap.setStatus(
        "current"
    )

panROUTINGRoutedECMPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1549)
)
panROUTINGRoutedECMPTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedECMPTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerMpExtensionNegotiateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1550)
)
panROUTINGRoutedBGPPeerMpExtensionNegotiateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerMpExtensionNegotiateTrap.setStatus(
        "current"
    )

panROUTINGPathMonitorFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1551)
)
panROUTINGPathMonitorFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGPathMonitorFailureTrap.setStatus(
        "current"
    )

panROUTINGPathMonitorRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1552)
)
panROUTINGPathMonitorRecoveryTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGPathMonitorRecoveryTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnRegistSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1600)
)
panSSLVPNSslvpnRegistSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnRegistSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnRegistFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1601)
)
panSSLVPNSslvpnRegistFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnRegistFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnLogoutSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1602)
)
panSSLVPNSslvpnLogoutSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnLogoutSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnLogoutFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1603)
)
panSSLVPNSslvpnLogoutFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnLogoutFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1604)
)
panSSLVPNSslvpnConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1605)
)
panSSLVPNSslvpnConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1606)
)
panSSLVPNSslvpnConfigReleaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigReleaseTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnSwitchSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1607)
)
panSSLVPNSslvpnSwitchSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnSwitchSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnSwitchFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1608)
)
panSSLVPNSslvpnSwitchFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnSwitchFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1609)
)
panSSLVPNSslvpnAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnAuthSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1610)
)
panSSLVPNSslvpnAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnAuthFailTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1700)
)
panVPNIkeConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1SuccessTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1701)
)
panVPNIkeConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1FailedTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1702)
)
panVPNIkeConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1AbortTrap.setStatus(
        "current"
    )

panVPNIkeConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1703)
)
panVPNIkeConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP2SuccessTrap.setStatus(
        "current"
    )

panVPNIkeConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1704)
)
panVPNIkeConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP2FailedTrap.setStatus(
        "current"
    )

panVPNIkeDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1705)
)
panVPNIkeDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonStartTrap.setStatus(
        "current"
    )

panVPNIkeDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1706)
)
panVPNIkeDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonExitTrap.setStatus(
        "current"
    )

panVPNIkeDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1707)
)
panVPNIkeDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonInitTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1StartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1708)
)
panVPNIkeNegoP1StartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1StartTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1709)
)
panVPNIkeNegoP1FailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1SuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1710)
)
panVPNIkeNegoP1SuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1SuccTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1ExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1711)
)
panVPNIkeNegoP1ExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1ExpireTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1712)
)
panVPNIkeNegoP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1DpdDnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1713)
)
panVPNIkeNegoP1DpdDnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1DpdDnTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1PskIdtypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1714)
)
panVPNIkeNegoP1PskIdtypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1PskIdtypeTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailPskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1715)
)
panVPNIkeNegoP1FailPskTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailPskTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailCommonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1716)
)
panVPNIkeNegoP1FailCommonTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailCommonTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2StartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1717)
)
panVPNIkeNegoP2StartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2StartTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1718)
)
panVPNIkeNegoP2FailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2FailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1719)
)
panVPNIkeNegoP2SuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SuccTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2StaleP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1720)
)
panVPNIkeNegoP2StaleP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2StaleP1Trap.setStatus(
        "current"
    )

panVPNIkeNegoP2DupRekeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1721)
)
panVPNIkeNegoP2DupRekeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2DupRekeyTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulContTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1722)
)
panVPNIkeNegoP2SimulContTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulContTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1723)
)
panVPNIkeNegoP2SimulFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulFailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1724)
)
panVPNIkeNegoP2SimulDelayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulDelayTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2NoP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1725)
)
panVPNIkeNegoP2NoP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2NoP1Trap.setStatus(
        "current"
    )

panVPNIkeNegoP2P1NotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1726)
)
panVPNIkeNegoP2P1NotReadyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2P1NotReadyTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2ProxyIdBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1727)
)
panVPNIkeNegoP2ProxyIdBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2ProxyIdBadTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2ProposalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1728)
)
panVPNIkeNegoP2ProposalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2ProposalBadTrap.setStatus(
        "current"
    )

panVPNIpsecKeyInstallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1729)
)
panVPNIpsecKeyInstallTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyInstallTrap.setStatus(
        "current"
    )

panVPNIpsecKeyDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1730)
)
panVPNIpsecKeyDeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyDeleteTrap.setStatus(
        "current"
    )

panVPNIpsecKeyExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1731)
)
panVPNIpsecKeyExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyExpireTrap.setStatus(
        "current"
    )

panVPNIkeRecvNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1732)
)
panVPNIkeRecvNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvNotifyTrap.setStatus(
        "current"
    )

panVPNIkeRecvP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1733)
)
panVPNIkeRecvP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeRecvP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1734)
)
panVPNIkeRecvP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkeSendNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1735)
)
panVPNIkeSendNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendNotifyTrap.setStatus(
        "current"
    )

panVPNIkeSendP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1736)
)
panVPNIkeSendP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeSendP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1737)
)
panVPNIkeSendP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1738)
)
panVPNIkev2NegoIkeStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeStartTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1739)
)
panVPNIkev2NegoIkeFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1740)
)
panVPNIkev2NegoIkeSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1741)
)
panVPNIkev2NegoIkeExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeExpireTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1742)
)
panVPNIkev2NegoIkeDeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeDeleteTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1743)
)
panVPNIkev2NegoChildStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildStartTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1744)
)
panVPNIkev2NegoChildFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1745)
)
panVPNIkev2NegoChildSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSuccTrap.setStatus(
        "current"
    )

panVPNTunnelStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1746)
)
panVPNTunnelStatusUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNTunnelStatusUpTrap.setStatus(
        "current"
    )

panVPNTunnelStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1747)
)
panVPNTunnelStatusDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNTunnelStatusDownTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1748)
)
panVPNKeymgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonStartTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1749)
)
panVPNKeymgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonExitTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1750)
)
panVPNKeymgrDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonInitTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1751)
)
panVPNKeymgrFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1752)
)
panVPNKeymgrFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1753)
)
panVPNKeymgrFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1754)
)
panVPNKeymgrIkeFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1755)
)
panVPNKeymgrIkeFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1756)
)
panVPNKeymgrIkeFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1757)
)
panVPNKeymgrHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1758)
)
panVPNKeymgrHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1759)
)
panVPNKeymgrHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNIkeGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1760)
)
panVPNIkeGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeGenericEventTrap.setStatus(
        "current"
    )

panVPNKeymgrGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1761)
)
panVPNKeymgrGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrGenericEventTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailCertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1762)
)
panVPNIkeNegoP1FailCertTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailCertTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1CertIdMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1763)
)
panVPNIkeNegoP1CertIdMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1CertIdMismatchTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1CertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1764)
)
panVPNIkeNegoP1CertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1CertSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeDpdDnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1765)
)
panVPNIkev2NegoIkeDpdDnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeDpdDnTrap.setStatus(
        "current"
    )

panVPNIkev2NegoPskIdtypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1766)
)
panVPNIkev2NegoPskIdtypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoPskIdtypeTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailPskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1767)
)
panVPNIkev2NegoFailPskTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailPskTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailCommonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1768)
)
panVPNIkev2NegoFailCommonTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailCommonTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailCertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1769)
)
panVPNIkev2NegoFailCertTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailCertTrap.setStatus(
        "current"
    )

panVPNIkev2NegoCertIdMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1770)
)
panVPNIkev2NegoCertIdMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoCertIdMismatchTrap.setStatus(
        "current"
    )

panVPNIkev2NegoCertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1771)
)
panVPNIkev2NegoCertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoCertSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoUseV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1772)
)
panVPNIkev2NegoUseV1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoUseV1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoStaleP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1773)
)
panVPNIkev2NegoStaleP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoStaleP1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoStaleP2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1774)
)
panVPNIkev2NegoStaleP2Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoStaleP2Trap.setStatus(
        "current"
    )

panVPNIkev2NegoChildDupRekeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1775)
)
panVPNIkev2NegoChildDupRekeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildDupRekeyTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulContTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1776)
)
panVPNIkev2NegoChildSimulContTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulContTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1777)
)
panVPNIkev2NegoChildSimulFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1778)
)
panVPNIkev2NegoChildSimulDelayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulDelayTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildNoP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1779)
)
panVPNIkev2NegoChildNoP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildNoP1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoChildP1NotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1780)
)
panVPNIkev2NegoChildP1NotReadyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildP1NotReadyTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildTsBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1781)
)
panVPNIkev2NegoChildTsBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildTsBadTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildProposalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1782)
)
panVPNIkev2NegoChildProposalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildProposalBadTrap.setStatus(
        "current"
    )

panVPNIkev2RecvNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1783)
)
panVPNIkev2RecvNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvNotifyTrap.setStatus(
        "current"
    )

panVPNIkev2RecvP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1784)
)
panVPNIkev2RecvP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2RecvP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1785)
)
panVPNIkev2RecvP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2SendNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1786)
)
panVPNIkev2SendNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendNotifyTrap.setStatus(
        "current"
    )

panVPNIkev2SendP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1787)
)
panVPNIkev2SendP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2SendP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1788)
)
panVPNIkev2SendP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendP2DeleteTrap.setStatus(
        "current"
    )

panVPNSdwanTunnelStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1789)
)
panVPNSdwanTunnelStatusUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNSdwanTunnelStatusUpTrap.setStatus(
        "current"
    )

panVPNSdwanTunnelStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1790)
)
panVPNSdwanTunnelStatusDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNSdwanTunnelStatusDownTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1800)
)
panSATDSatdConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1SuccessTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1801)
)
panSATDSatdConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1FailedTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1802)
)
panSATDSatdConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1AbortTrap.setStatus(
        "current"
    )

panSATDSatdConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1803)
)
panSATDSatdConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP2SuccessTrap.setStatus(
        "current"
    )

panSATDSatdConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1804)
)
panSATDSatdConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP2FailedTrap.setStatus(
        "current"
    )

panSATDSatdDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1805)
)
panSATDSatdDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonStartTrap.setStatus(
        "current"
    )

panSATDSatdDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1806)
)
panSATDSatdDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonExitTrap.setStatus(
        "current"
    )

panSATDSatdDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1807)
)
panSATDSatdDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonInitTrap.setStatus(
        "current"
    )

panSATDSatdTunUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1808)
)
panSATDSatdTunUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunUpTrap.setStatus(
        "current"
    )

panSATDSatdTunDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1809)
)
panSATDSatdTunDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunDownTrap.setStatus(
        "current"
    )

panSATDSatdDupSubnetsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1810)
)
panSATDSatdDupSubnetsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDupSubnetsTrap.setStatus(
        "current"
    )

panSATDSatdDeniedRoutesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1811)
)
panSATDSatdDeniedRoutesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDeniedRoutesTrap.setStatus(
        "current"
    )

panSATDSatdPortalGatewayDuplicateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1812)
)
panSATDSatdPortalGatewayDuplicateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalGatewayDuplicateTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1813)
)
panSATDSatdFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncStartTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1814)
)
panSATDSatdFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1815)
)
panSATDSatdFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1816)
)
panSATDSatdHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncStartTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1817)
)
panSATDSatdHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncAbortTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1818)
)
panSATDSatdHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncDoneTrap.setStatus(
        "current"
    )

panSATDSatdIpAssignFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1819)
)
panSATDSatdIpAssignFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdIpAssignFailTrap.setStatus(
        "current"
    )

panSATDSatdIpResetFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1820)
)
panSATDSatdIpResetFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdIpResetFailTrap.setStatus(
        "current"
    )

panSATDSatdTunMonDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1821)
)
panSATDSatdTunMonDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunMonDownTrap.setStatus(
        "current"
    )

panSATDSatdTunMonUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1822)
)
panSATDSatdTunMonUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunMonUpTrap.setStatus(
        "current"
    )

panSATDSatdTunSoftlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1823)
)
panSATDSatdTunSoftlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunSoftlifetimeExpiredTrap.setStatus(
        "current"
    )

panSATDSatdTunHardlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1824)
)
panSATDSatdTunHardlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunHardlifetimeExpiredTrap.setStatus(
        "current"
    )

panSATDSatdAccRouteUpdFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1825)
)
panSATDSatdAccRouteUpdFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdAccRouteUpdFailTrap.setStatus(
        "current"
    )

panSATDSatdNhUpdFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1826)
)
panSATDSatdNhUpdFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdNhUpdFailTrap.setStatus(
        "current"
    )

panSATDSatdTunDpInstallErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1827)
)
panSATDSatdTunDpInstallErrTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunDpInstallErrTrap.setStatus(
        "current"
    )

panSATDSatdGatewayConnectStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1828)
)
panSATDSatdGatewayConnectStartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGatewayConnectStartedTrap.setStatus(
        "current"
    )

panSATDSatdPortalConnectStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1829)
)
panSATDSatdPortalConnectStartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalConnectStartedTrap.setStatus(
        "current"
    )

panSATDSatdGatewayConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1830)
)
panSATDSatdGatewayConnectFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGatewayConnectFailedTrap.setStatus(
        "current"
    )

panSATDSatdPortalConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1831)
)
panSATDSatdPortalConnectFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalConnectFailedTrap.setStatus(
        "current"
    )

panSATDSatdGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1832)
)
panSATDSatdGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGenericEventTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1900)
)
panSSLMGRSslmgrConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1SuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1901)
)
panSSLMGRSslmgrConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1FailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1902)
)
panSSLMGRSslmgrConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1AbortTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1903)
)
panSSLMGRSslmgrConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP2SuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1904)
)
panSSLMGRSslmgrConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP2FailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1905)
)
panSSLMGRSslmgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrDaemonStartTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1906)
)
panSSLMGRSslmgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrDaemonExitTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertGenSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1907)
)
panSSLMGRSslmgrCertGenSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertGenSuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertGenFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1908)
)
panSSLMGRSslmgrCertGenFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertGenFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertStatusDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1909)
)
panSSLMGRSslmgrCertStatusDeletedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertStatusDeletedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertStatusRevokedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1910)
)
panSSLMGRSslmgrCertStatusRevokedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertStatusRevokedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1911)
)
panSSLMGRSslmgrSatelliteInfoInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoInsertedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1912)
)
panSSLMGRSslmgrSatelliteInfoUpdatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoUpdatedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1913)
)
panSSLMGRSslmgrSatelliteInfoDeletedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoDeletedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertOcspVerifyFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1914)
)
panSSLMGRSslmgrCertOcspVerifyFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertOcspVerifyFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertCrlVerifyFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1915)
)
panSSLMGRSslmgrCertCrlVerifyFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertCrlVerifyFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrHaFullSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1916)
)
panSSLMGRSslmgrHaFullSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrHaFullSyncTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrHaNotFullSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1917)
)
panSSLMGRSslmgrHaNotFullSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrHaNotFullSyncTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1918)
)
panSSLMGRSslmgrGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrGenericEventTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrScepCertSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1919)
)
panSSLMGRSslmgrScepCertSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrScepCertSuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrScepCertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1920)
)
panSSLMGRSslmgrScepCertFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrScepCertFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrScepCaCertSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1921)
)
panSSLMGRSslmgrScepCaCertSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrScepCaCertSuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrScepCaCertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1922)
)
panSSLMGRSslmgrScepCaCertFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrScepCaCertFailedTrap.setStatus(
        "current"
    )

panSSLMGRCaSessionEstablishmentSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1923)
)
panSSLMGRCaSessionEstablishmentSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRCaSessionEstablishmentSuccessTrap.setStatus(
        "current"
    )

panSSLMGRCaSessionEstablishmentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1924)
)
panSSLMGRCaSessionEstablishmentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRCaSessionEstablishmentFailedTrap.setStatus(
        "current"
    )

panURLNoUrlDatabaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2000)
)
panURLNoUrlDatabaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLNoUrlDatabaseTrap.setStatus(
        "current"
    )

panURLInvalidLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2001)
)
panURLInvalidLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLInvalidLicenseTrap.setStatus(
        "current"
    )

panURLFailedToLockUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2002)
)
panURLFailedToLockUpdateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLFailedToLockUpdateTrap.setStatus(
        "current"
    )

panURLConnectionSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2003)
)
panURLConnectionSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLConnectionSuccessTrap.setStatus(
        "current"
    )

panURLConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2004)
)
panURLConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLConnectionFailureTrap.setStatus(
        "current"
    )

panURLServerIsDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2005)
)
panURLServerIsDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLServerIsDownTrap.setStatus(
        "current"
    )

panURLProxyConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2006)
)
panURLProxyConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLProxyConnectionFailureTrap.setStatus(
        "current"
    )

panURLReceiveDataFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2007)
)
panURLReceiveDataFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLReceiveDataFailureTrap.setStatus(
        "current"
    )

panURLDynamicUrlConnectionDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2008)
)
panURLDynamicUrlConnectionDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDynamicUrlConnectionDownTrap.setStatus(
        "current"
    )

panURLDownloadingUrlDatabaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2009)
)
panURLDownloadingUrlDatabaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadingUrlDatabaseTrap.setStatus(
        "current"
    )

panURLDownloadUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2010)
)
panURLDownloadUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLUpgradeUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2011)
)
panURLUpgradeUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUpgradeUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLRevertUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2012)
)
panURLRevertUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRevertUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLUrlDatabaseIsLatestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2013)
)
panURLUrlDatabaseIsLatestTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlDatabaseIsLatestTrap.setStatus(
        "current"
    )

panURLUrlDownloadFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2014)
)
panURLUrlDownloadFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlDownloadFailureTrap.setStatus(
        "current"
    )

panURLUrlCloudConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2015)
)
panURLUrlCloudConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlCloudConnectionFailureTrap.setStatus(
        "current"
    )

panURLUrlCloudConnectionSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2016)
)
panURLUrlCloudConnectionSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlCloudConnectionSuccessTrap.setStatus(
        "current"
    )

panURLUrlBackupSeedSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2017)
)
panURLUrlBackupSeedSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlBackupSeedSuccessTrap.setStatus(
        "current"
    )

panURLUrlBackupSeedFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2018)
)
panURLUrlBackupSeedFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlBackupSeedFailureTrap.setStatus(
        "current"
    )

panURLCloudElectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2019)
)
panURLCloudElectionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudElectionTrap.setStatus(
        "current"
    )

panURLCloudProcessStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2020)
)
panURLCloudProcessStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudProcessStartsTrap.setStatus(
        "current"
    )

panURLCloudProcessStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2021)
)
panURLCloudProcessStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudProcessStoppedTrap.setStatus(
        "current"
    )

panURLUpdateVersionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2022)
)
panURLUpdateVersionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUpdateVersionFailureTrap.setStatus(
        "current"
    )

panURLErrorMsgFromCloudTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2023)
)
panURLErrorMsgFromCloudTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLErrorMsgFromCloudTrap.setStatus(
        "current"
    )

panURLTestASiteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2024)
)
panURLTestASiteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLTestASiteTrap.setStatus(
        "current"
    )

panURLUrlEngineStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2025)
)
panURLUrlEngineStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlEngineStoppedTrap.setStatus(
        "current"
    )

panURLUrlEngineStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2026)
)
panURLUrlEngineStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlEngineStartsTrap.setStatus(
        "current"
    )

panURLStartupFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2027)
)
panURLStartupFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartupFailureTrap.setStatus(
        "current"
    )

panURLHaSyncFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2028)
)
panURLHaSyncFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLHaSyncFailureTrap.setStatus(
        "current"
    )

panURLHaSyncSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2029)
)
panURLHaSyncSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLHaSyncSuccessTrap.setStatus(
        "current"
    )

panURLSaveMpCacheToDiscFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2030)
)
panURLSaveMpCacheToDiscFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSaveMpCacheToDiscFailureTrap.setStatus(
        "current"
    )

panURLSaveMpCacheToDiscSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2031)
)
panURLSaveMpCacheToDiscSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSaveMpCacheToDiscSuccessTrap.setStatus(
        "current"
    )

panURLRfsProcessStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2032)
)
panURLRfsProcessStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessStartsTrap.setStatus(
        "current"
    )

panURLRfsProcessStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2033)
)
panURLRfsProcessStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessStoppedTrap.setStatus(
        "current"
    )

panURLRfsProcessFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2034)
)
panURLRfsProcessFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessFailureTrap.setStatus(
        "current"
    )

panURLRequestToCloudFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2035)
)
panURLRequestToCloudFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRequestToCloudFailureTrap.setStatus(
        "current"
    )

panURLStartsFromEmptySeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2036)
)
panURLStartsFromEmptySeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromEmptySeedTrap.setStatus(
        "current"
    )

panURLLoadSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2037)
)
panURLLoadSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLLoadSuccessTrap.setStatus(
        "current"
    )

panURLFailedToLockDownloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2038)
)
panURLFailedToLockDownloadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLFailedToLockDownloadTrap.setStatus(
        "current"
    )

panURLEngineStartupFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2039)
)
panURLEngineStartupFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLEngineStartupFailureTrap.setStatus(
        "current"
    )

panURLSeedOutOfSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2040)
)
panURLSeedOutOfSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSeedOutOfSyncTrap.setStatus(
        "current"
    )

panURLStartsFromBackupSeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2041)
)
panURLStartsFromBackupSeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromBackupSeedTrap.setStatus(
        "current"
    )

panURLStartsFromDownloadSeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2042)
)
panURLStartsFromDownloadSeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromDownloadSeedTrap.setStatus(
        "current"
    )

panURLBackupSeedErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2043)
)
panURLBackupSeedErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLBackupSeedErrorTrap.setStatus(
        "current"
    )

panURLDownloadSeedErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2044)
)
panURLDownloadSeedErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadSeedErrorTrap.setStatus(
        "current"
    )

panUSERIDConnectAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2300)
)
panUSERIDConnectAgentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectAgentTrap.setStatus(
        "current"
    )

panUSERIDDisconnectAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2301)
)
panUSERIDDisconnectAgentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectAgentTrap.setStatus(
        "current"
    )

panUSERIDAgentEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2302)
)
panUSERIDAgentEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentEventTrap.setStatus(
        "current"
    )

panUSERIDConnectAgentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2303)
)
panUSERIDConnectAgentFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectAgentFailureTrap.setStatus(
        "current"
    )

panUSERIDAgentVersionMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2304)
)
panUSERIDAgentVersionMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentVersionMismatchTrap.setStatus(
        "current"
    )

panUSERIDAgentStatusFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2305)
)
panUSERIDAgentStatusFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentStatusFailureTrap.setStatus(
        "current"
    )

panUSERIDAgentReadLogErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2306)
)
panUSERIDAgentReadLogErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentReadLogErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetDomainErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2307)
)
panUSERIDAgentGetDomainErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetDomainErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetUsersErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2308)
)
panUSERIDAgentGetUsersErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetUsersErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetGroupsErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2309)
)
panUSERIDAgentGetGroupsErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetGroupsErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetConfigErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2310)
)
panUSERIDAgentGetConfigErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetConfigErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentNoDomainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2311)
)
panUSERIDAgentNoDomainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentNoDomainTrap.setStatus(
        "current"
    )

panUSERIDAgentNoAllowlistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2312)
)
panUSERIDAgentNoAllowlistTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentNoAllowlistTrap.setStatus(
        "current"
    )

panUSERIDConnectLdapSeverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2313)
)
panUSERIDConnectLdapSeverTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectLdapSeverTrap.setStatus(
        "current"
    )

panUSERIDConnectLdapSeverFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2314)
)
panUSERIDConnectLdapSeverFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectLdapSeverFailureTrap.setStatus(
        "current"
    )

panUSERIDGetLdapDataFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2315)
)
panUSERIDGetLdapDataFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDGetLdapDataFailureTrap.setStatus(
        "current"
    )

panUSERIDHAQueueFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2316)
)
panUSERIDHAQueueFullTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDHAQueueFullTrap.setStatus(
        "current"
    )

panUSERIDConnectClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2317)
)
panUSERIDConnectClientTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectClientTrap.setStatus(
        "current"
    )

panUSERIDDisconnectClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2318)
)
panUSERIDDisconnectClientTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectClientTrap.setStatus(
        "current"
    )

panUSERIDConnectServerMonitorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2319)
)
panUSERIDConnectServerMonitorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectServerMonitorTrap.setStatus(
        "current"
    )

panUSERIDConnectServerMonitorFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2320)
)
panUSERIDConnectServerMonitorFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectServerMonitorFailureTrap.setStatus(
        "current"
    )

panUSERIDConnectVmInfoSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2321)
)
panUSERIDConnectVmInfoSourceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectVmInfoSourceTrap.setStatus(
        "current"
    )

panUSERIDDisconnectVmInfoSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2322)
)
panUSERIDDisconnectVmInfoSourceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectVmInfoSourceTrap.setStatus(
        "current"
    )

panUSERIDConnectVmInfoSourceFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2323)
)
panUSERIDConnectVmInfoSourceFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectVmInfoSourceFailureTrap.setStatus(
        "current"
    )

panUSERIDRegisteredIpUpdateFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2324)
)
panUSERIDRegisteredIpUpdateFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDRegisteredIpUpdateFailureTrap.setStatus(
        "current"
    )

panUSERIDConnectSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2325)
)
panUSERIDConnectSyslogTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectSyslogTrap.setStatus(
        "current"
    )

panUSERIDDisconnectSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2326)
)
panUSERIDDisconnectSyslogTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectSyslogTrap.setStatus(
        "current"
    )

panUSERIDUserGroupCountTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2327)
)
panUSERIDUserGroupCountTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDUserGroupCountTrap.setStatus(
        "current"
    )

panUSERIDUserCountTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2328)
)
panUSERIDUserCountTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDUserCountTrap.setStatus(
        "current"
    )

panUSERIDGlobalprotectgatewayInvalidLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2329)
)
panUSERIDGlobalprotectgatewayInvalidLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDGlobalprotectgatewayInvalidLicenseTrap.setStatus(
        "current"
    )

panNATFallbackReportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2400)
)
panNATFallbackReportTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNATFallbackReportTrap.setStatus(
        "current"
    )

panSYSLOGNGSyslogConnStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2500)
)
panSYSLOGNGSyslogConnStatusTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSYSLOGNGSyslogConnStatusTrap.setStatus(
        "current"
    )

panLACPLostConnectivityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2600)
)
panLACPLostConnectivityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLostConnectivityTrap.setStatus(
        "current"
    )

panLACPUnresponsiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2601)
)
panLACPUnresponsiveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPUnresponsiveTrap.setStatus(
        "current"
    )

panLACPNegoFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2602)
)
panLACPNegoFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPNegoFailTrap.setStatus(
        "current"
    )

panLACPSpeedDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2603)
)
panLACPSpeedDuplexTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPSpeedDuplexTrap.setStatus(
        "current"
    )

panLACPLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2604)
)
panLACPLinkDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLinkDownTrap.setStatus(
        "current"
    )

panLACPLacpDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2605)
)
panLACPLacpDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLacpDownTrap.setStatus(
        "current"
    )

panLACPLacpUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2606)
)
panLACPLacpUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLacpUpTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2700)
)
panFIPSFipsSelftestUnknownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestUnknownTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2701)
)
panFIPSFipsSelftestTimeoutTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestTimeoutTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestIntegTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2702)
)
panFIPSFipsSelftestIntegTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestIntegTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestCoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2703)
)
panFIPSFipsSelftestCoreTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestCoreTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestAesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2704)
)
panFIPSFipsSelftestAesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestAesTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2705)
)
panFIPSFipsSelftestDesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDesTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2706)
)
panFIPSFipsSelftestDsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestRsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2707)
)
panFIPSFipsSelftestRsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestRsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestHmacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2708)
)
panFIPSFipsSelftestHmacTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestHmacTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestShaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2709)
)
panFIPSFipsSelftestShaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestShaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2710)
)
panFIPSFipsSelftestDrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestNdrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2711)
)
panFIPSFipsSelftestNdrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestNdrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDhParameterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2712)
)
panFIPSFipsSelftestDhParameterTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDhParameterTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDhTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2713)
)
panFIPSFipsSelftestDhTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDhTrap.setStatus(
        "current"
    )

panFIPSFipsFirmwareIntegrityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2714)
)
panFIPSFipsFirmwareIntegrityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsFirmwareIntegrityTrap.setStatus(
        "current"
    )

panFIPSFipsContinuousRngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2715)
)
panFIPSFipsContinuousRngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsContinuousRngTrap.setStatus(
        "current"
    )

panFIPSFipsRsaPairwiseConsistencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2716)
)
panFIPSFipsRsaPairwiseConsistencyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsRsaPairwiseConsistencyTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestSoftwareLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2717)
)
panFIPSFipsSelftestSoftwareLoadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestSoftwareLoadTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2718)
)
panFIPSFipsSelftestTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestHsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2719)
)
panFIPSFipsSelftestHsmTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestHsmTrap.setStatus(
        "current"
    )

panFIPSFipsZeroizationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2720)
)
panFIPSFipsZeroizationTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsZeroizationTrap.setStatus(
        "current"
    )

panFIPSFipsKeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2721)
)
panFIPSFipsKeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsKeyTrap.setStatus(
        "current"
    )

panFIPSFipsCipherTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2722)
)
panFIPSFipsCipherTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsCipherTrap.setStatus(
        "current"
    )

panFIPSFipsReplayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2723)
)
panFIPSFipsReplayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsReplayTrap.setStatus(
        "current"
    )

panFIPSFipsSslHandshakeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2724)
)
panFIPSFipsSslHandshakeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSslHandshakeTrap.setStatus(
        "current"
    )

panFIPSFipsContinuousNdrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2725)
)
panFIPSFipsContinuousNdrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsContinuousNdrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestCmacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2726)
)
panFIPSFipsSelftestCmacTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestCmacTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDrbgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2727)
)
panFIPSFipsSelftestDrbgTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDrbgTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestEcdsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2728)
)
panFIPSFipsSelftestEcdsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestEcdsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestEcdhTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2729)
)
panFIPSFipsSelftestEcdhTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestEcdhTrap.setStatus(
        "current"
    )

panMDMExceedLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2800)
)
panMDMExceedLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMExceedLicenseTrap.setStatus(
        "current"
    )

panMDMConnectToApnsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2801)
)
panMDMConnectToApnsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToApnsTrap.setStatus(
        "current"
    )

panMDMConnectToApnsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2802)
)
panMDMConnectToApnsFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToApnsFailureTrap.setStatus(
        "current"
    )

panMDMConnectToGcmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2803)
)
panMDMConnectToGcmTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToGcmTrap.setStatus(
        "current"
    )

panMDMConnectToGcmFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2804)
)
panMDMConnectToGcmFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToGcmFailureTrap.setStatus(
        "current"
    )

panMDMGatewayConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2805)
)
panMDMGatewayConnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGatewayConnectedTrap.setStatus(
        "current"
    )

panMDMGatewayDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2806)
)
panMDMGatewayDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGatewayDisconnectedTrap.setStatus(
        "current"
    )

panMDMInstallAppContentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2807)
)
panMDMInstallAppContentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMInstallAppContentTrap.setStatus(
        "current"
    )

panMDMInstallAppContentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2808)
)
panMDMInstallAppContentFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMInstallAppContentFailureTrap.setStatus(
        "current"
    )

panMDMGetScepOtpFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2809)
)
panMDMGetScepOtpFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGetScepOtpFailureTrap.setStatus(
        "current"
    )

panMDMSendMsgToCloudFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2810)
)
panMDMSendMsgToCloudFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMSendMsgToCloudFailureTrap.setStatus(
        "current"
    )

panMDMConnectToItunesFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2811)
)
panMDMConnectToItunesFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToItunesFailureTrap.setStatus(
        "current"
    )

panMDMConnectToAppleVppFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2812)
)
panMDMConnectToAppleVppFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToAppleVppFailureTrap.setStatus(
        "current"
    )

panRAIDDiskNotDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2900)
)
panRAIDDiskNotDetectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskNotDetectedTrap.setStatus(
        "current"
    )

panRAIDPairDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2901)
)
panRAIDPairDetectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDetectedTrap.setStatus(
        "current"
    )

panRAIDRebuildingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2902)
)
panRAIDRebuildingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildingTrap.setStatus(
        "current"
    )

panRAIDRebuild20Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2903)
)
panRAIDRebuild20Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild20Trap.setStatus(
        "current"
    )

panRAIDRebuild40Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2904)
)
panRAIDRebuild40Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild40Trap.setStatus(
        "current"
    )

panRAIDRebuild60Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2905)
)
panRAIDRebuild60Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild60Trap.setStatus(
        "current"
    )

panRAIDRebuild80Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2906)
)
panRAIDRebuild80Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild80Trap.setStatus(
        "current"
    )

panRAIDRebuildDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2907)
)
panRAIDRebuildDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildDoneTrap.setStatus(
        "current"
    )

panRAIDDiskActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2908)
)
panRAIDDiskActiveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskActiveTrap.setStatus(
        "current"
    )

panRAIDDiskFaultyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2909)
)
panRAIDDiskFaultyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskFaultyTrap.setStatus(
        "current"
    )

panRAIDDiskFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2910)
)
panRAIDDiskFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskFailedTrap.setStatus(
        "current"
    )

panRAIDSpareMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2911)
)
panRAIDSpareMissingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDSpareMissingTrap.setStatus(
        "current"
    )

panRAIDSpareMovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2912)
)
panRAIDSpareMovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDSpareMovedTrap.setStatus(
        "current"
    )

panRAIDPairDegradedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2913)
)
panRAIDPairDegradedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDegradedTrap.setStatus(
        "current"
    )

panRAIDPairDisappearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2914)
)
panRAIDPairDisappearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDisappearedTrap.setStatus(
        "current"
    )

panRAIDDiskRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2915)
)
panRAIDDiskRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskRemovedTrap.setStatus(
        "current"
    )

panRAIDFsckStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2916)
)
panRAIDFsckStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckStartTrap.setStatus(
        "current"
    )

panRAIDFsckEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2917)
)
panRAIDFsckEndTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckEndTrap.setStatus(
        "current"
    )

panRAIDFsckFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2918)
)
panRAIDFsckFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckFailedTrap.setStatus(
        "current"
    )

panRAIDMountFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2919)
)
panRAIDMountFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDMountFailedTrap.setStatus(
        "current"
    )

panRAIDRebuildFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2920)
)
panRAIDRebuildFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildFailedTrap.setStatus(
        "current"
    )

panVMDvfInitSucceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3000)
)
panVMDvfInitSucceedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVMDvfInitSucceedTrap.setStatus(
        "current"
    )

panVMDvfInitFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3001)
)
panVMDvfInitFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVMDvfInitFailTrap.setStatus(
        "current"
    )

panSSHSshSessionEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3100)
)
panSSHSshSessionEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionEstablishedTrap.setStatus(
        "current"
    )

panSSHSshSessionTerminatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3101)
)
panSSHSshSessionTerminatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionTerminatedTrap.setStatus(
        "current"
    )

panSSHSshSessionEstablishmentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3102)
)
panSSHSshSessionEstablishmentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionEstablishmentFailedTrap.setStatus(
        "current"
    )

panSSHSshSessionDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3103)
)
panSSHSshSessionDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionDisconnectedTrap.setStatus(
        "current"
    )

panSSHSshConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3104)
)
panSSHSshConnectionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshConnectionTrap.setStatus(
        "current"
    )

panTLSTlsSessionEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3200)
)
panTLSTlsSessionEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionEstablishedTrap.setStatus(
        "current"
    )

panTLSTlsSessionTerminatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3201)
)
panTLSTlsSessionTerminatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionTerminatedTrap.setStatus(
        "current"
    )

panTLSTlsSessionEstablishmentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3202)
)
panTLSTlsSessionEstablishmentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionEstablishmentFailedTrap.setStatus(
        "current"
    )

panTLSTlsSessionDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3203)
)
panTLSTlsSessionDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionDisconnectedTrap.setStatus(
        "current"
    )

panTLSTlsEdlAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3204)
)
panTLSTlsEdlAuthFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsEdlAuthFailureTrap.setStatus(
        "current"
    )

panTLSTlsX509ServerIdentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3205)
)
panTLSTlsX509ServerIdentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509ServerIdentFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509ValidationFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3206)
)
panTLSTlsX509ValidationFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509ValidationFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509EkuServerAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3207)
)
panTLSTlsX509EkuServerAuthFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509EkuServerAuthFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509ClientIdentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3208)
)
panTLSTlsX509ClientIdentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509ClientIdentFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509EkuClientAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3209)
)
panTLSTlsX509EkuClientAuthFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509EkuClientAuthFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509EkuClientAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3210)
)
panTLSTlsX509EkuClientAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509EkuClientAuthSuccessTrap.setStatus(
        "current"
    )

panTLSPanoramaAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3211)
)
panTLSPanoramaAuthFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSPanoramaAuthFailureTrap.setStatus(
        "current"
    )

panTLSPanoramaAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3212)
)
panTLSPanoramaAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSPanoramaAuthSuccessTrap.setStatus(
        "current"
    )

panTLSPanosAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3213)
)
panTLSPanosAuthFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSPanosAuthFailureTrap.setStatus(
        "current"
    )

panTLSPanosAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3214)
)
panTLSPanosAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSPanosAuthSuccessTrap.setStatus(
        "current"
    )

panTLSTlsX509EkuCodeSigningExtCheckFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3215)
)
panTLSTlsX509EkuCodeSigningExtCheckFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509EkuCodeSigningExtCheckFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509OcspCrlCheckFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3216)
)
panTLSTlsX509OcspCrlCheckFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509OcspCrlCheckFailedTrap.setStatus(
        "current"
    )

panTLSTlsX509UntrustedCertIssuerFoundTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3217)
)
panTLSTlsX509UntrustedCertIssuerFoundTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsX509UntrustedCertIssuerFoundTrap.setStatus(
        "current"
    )

panTLSMfaAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3218)
)
panTLSMfaAuthFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSMfaAuthFailureTrap.setStatus(
        "current"
    )

panTLSCertificateRenewalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3219)
)
panTLSCertificateRenewalTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSCertificateRenewalTrap.setStatus(
        "current"
    )

panTLSCertificateExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3220)
)
panTLSCertificateExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSCertificateExpiredTrap.setStatus(
        "current"
    )

panLLDPRxErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3300)
)
panLLDPRxErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPRxErrorTrap.setStatus(
        "current"
    )

panLLDPMibChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3301)
)
panLLDPMibChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPMibChangedTrap.setStatus(
        "current"
    )

panLLDPTooManyNeighborsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3302)
)
panLLDPTooManyNeighborsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTooManyNeighborsTrap.setStatus(
        "current"
    )

panLLDPTooManyNeighborsTimerClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3303)
)
panLLDPTooManyNeighborsTimerClearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTooManyNeighborsTimerClearedTrap.setStatus(
        "current"
    )

panLLDPOtherTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3304)
)
panLLDPOtherTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPOtherTrap.setStatus(
        "current"
    )

panLLDPTxErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3305)
)
panLLDPTxErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTxErrorTrap.setStatus(
        "current"
    )

panFBWildfireWrongCloudTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3400)
)
panFBWildfireWrongCloudTypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireWrongCloudTypeTrap.setStatus(
        "current"
    )

panFBWildfireDisabledByCloudTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3401)
)
panFBWildfireDisabledByCloudTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireDisabledByCloudTrap.setStatus(
        "current"
    )

panFBWildfireNoPolicyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3402)
)
panFBWildfireNoPolicyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireNoPolicyTrap.setStatus(
        "current"
    )

panFBWildfireNoLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3403)
)
panFBWildfireNoLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireNoLicenseTrap.setStatus(
        "current"
    )

panFBWildfireInvalidCloudInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3404)
)
panFBWildfireInvalidCloudInfoTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireInvalidCloudInfoTrap.setStatus(
        "current"
    )

panBFDExpiredTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3500)
)
panBFDExpiredTimeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panBFDExpiredTimeTrap.setStatus(
        "current"
    )

panBFDNeighborDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3501)
)
panBFDNeighborDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panBFDNeighborDownTrap.setStatus(
        "current"
    )

panBFDForwardPlaneResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3502)
)
panBFDForwardPlaneResetTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panBFDForwardPlaneResetTrap.setStatus(
        "current"
    )

panBFDAdminDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3503)
)
panBFDAdminDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panBFDAdminDownTrap.setStatus(
        "current"
    )

panBFDSessionStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3504)
)
panBFDSessionStateChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panBFDSessionStateChangeTrap.setStatus(
        "current"
    )

panAUTHGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3600)
)
panAUTHGeneralTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHGeneralTrap.setStatus(
        "current"
    )

panAUTHAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3601)
)
panAUTHAuthServerDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHAuthServerDownTrap.setStatus(
        "current"
    )

panAUTHCreateAdminAcctErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3602)
)
panAUTHCreateAdminAcctErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHCreateAdminAcctErrorTrap.setStatus(
        "current"
    )

panAUTHAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3603)
)
panAUTHAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHAuthFailTrap.setStatus(
        "current"
    )

panAUTHAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3604)
)
panAUTHAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHAuthSuccessTrap.setStatus(
        "current"
    )

panAUTHSamlClientRedirectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3605)
)
panAUTHSamlClientRedirectTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlClientRedirectTrap.setStatus(
        "current"
    )

panAUTHSamlIdpActivityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3606)
)
panAUTHSamlIdpActivityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlIdpActivityTrap.setStatus(
        "current"
    )

panAUTHSamlCertificateWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3607)
)
panAUTHSamlCertificateWarningTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlCertificateWarningTrap.setStatus(
        "current"
    )

panAUTHSamlCertificateErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3608)
)
panAUTHSamlCertificateErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlCertificateErrorTrap.setStatus(
        "current"
    )

panAUTHSamlMessageParseErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3609)
)
panAUTHSamlMessageParseErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlMessageParseErrorTrap.setStatus(
        "current"
    )

panAUTHSamlOutOfBandMessageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3610)
)
panAUTHSamlOutOfBandMessageTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlOutOfBandMessageTrap.setStatus(
        "current"
    )

panAUTHSamlSignatureValidatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3611)
)
panAUTHSamlSignatureValidatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSamlSignatureValidatedTrap.setStatus(
        "current"
    )

panAUTHEdlCliAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3612)
)
panAUTHEdlCliAuthFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHEdlCliAuthFailureTrap.setStatus(
        "current"
    )

panAUTHLogoutSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3613)
)
panAUTHLogoutSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHLogoutSuccessTrap.setStatus(
        "current"
    )

panAUTHLogoutFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3614)
)
panAUTHLogoutFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHLogoutFailedTrap.setStatus(
        "current"
    )

panAUTHIdpInitiatedLogOutSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3615)
)
panAUTHIdpInitiatedLogOutSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHIdpInitiatedLogOutSuccessTrap.setStatus(
        "current"
    )

panAUTHSpInitiatedLogOutSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3616)
)
panAUTHSpInitiatedLogOutSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHSpInitiatedLogOutSuccessTrap.setStatus(
        "current"
    )

panAUTHUserPasswordChangeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3617)
)
panAUTHUserPasswordChangeSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHUserPasswordChangeSuccessTrap.setStatus(
        "current"
    )

panAUTHUserPasswordChangeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3618)
)
panAUTHUserPasswordChangeFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panAUTHUserPasswordChangeFailedTrap.setStatus(
        "current"
    )

panCLUSTERDClusterDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3700)
)
panCLUSTERDClusterDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterDaemonInitTrap.setStatus(
        "current"
    )

panCLUSTERDClusterDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3701)
)
panCLUSTERDClusterDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterDaemonStartTrap.setStatus(
        "current"
    )

panCLUSTERDClusterDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3702)
)
panCLUSTERDClusterDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterDaemonExitTrap.setStatus(
        "current"
    )

panCLUSTERDClusterDaemonCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3703)
)
panCLUSTERDClusterDaemonCfgTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterDaemonCfgTrap.setStatus(
        "current"
    )

panCLUSTERDClusterDaemonCfgGiveupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3704)
)
panCLUSTERDClusterDaemonCfgGiveupTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterDaemonCfgGiveupTrap.setStatus(
        "current"
    )

panCLUSTERDClusterHaSyncPeerBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3705)
)
panCLUSTERDClusterHaSyncPeerBackupTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterHaSyncPeerBackupTrap.setStatus(
        "current"
    )

panCLUSTERDClusterHaSyncSelfMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3706)
)
panCLUSTERDClusterHaSyncSelfMasterTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterHaSyncSelfMasterTrap.setStatus(
        "current"
    )

panCLUSTERDClusterConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3707)
)
panCLUSTERDClusterConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterConfigP1SuccessTrap.setStatus(
        "current"
    )

panCLUSTERDClusterConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3708)
)
panCLUSTERDClusterConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterConfigP1FailedTrap.setStatus(
        "current"
    )

panCLUSTERDClusterConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3709)
)
panCLUSTERDClusterConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterConfigP1AbortTrap.setStatus(
        "current"
    )

panCLUSTERDClusterConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3710)
)
panCLUSTERDClusterConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterConfigP2SuccessTrap.setStatus(
        "current"
    )

panCLUSTERDClusterConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3711)
)
panCLUSTERDClusterConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterConfigP2FailedTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineControllerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3712)
)
panCLUSTERDClusterEngineControllerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineControllerTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3713)
)
panCLUSTERDClusterEngineServerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineServerTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineWorkerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3714)
)
panCLUSTERDClusterEngineWorkerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineWorkerTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineReloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3715)
)
panCLUSTERDClusterEngineReloadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineReloadTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3716)
)
panCLUSTERDClusterEngineRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineRestartTrap.setStatus(
        "current"
    )

panCLUSTERDClusterEngineShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3717)
)
panCLUSTERDClusterEngineShutdownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterEngineShutdownTrap.setStatus(
        "current"
    )

panCLUSTERDClusterSelfJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3718)
)
panCLUSTERDClusterSelfJoinTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterSelfJoinTrap.setStatus(
        "current"
    )

panCLUSTERDClusterSelfDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3719)
)
panCLUSTERDClusterSelfDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterSelfDownTrap.setStatus(
        "current"
    )

panCLUSTERDClusterSelfLeaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3720)
)
panCLUSTERDClusterSelfLeaveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterSelfLeaveTrap.setStatus(
        "current"
    )

panCLUSTERDClusterOtherJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3721)
)
panCLUSTERDClusterOtherJoinTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterOtherJoinTrap.setStatus(
        "current"
    )

panCLUSTERDClusterOtherDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3722)
)
panCLUSTERDClusterOtherDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterOtherDownTrap.setStatus(
        "current"
    )

panCLUSTERDClusterOtherLeaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3723)
)
panCLUSTERDClusterOtherLeaveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCLUSTERDClusterOtherLeaveTrap.setStatus(
        "current"
    )

panIPV6NDIpv6DisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3800)
)
panIPV6NDIpv6DisabledTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panIPV6NDIpv6DisabledTrap.setStatus(
        "current"
    )

panIPV6NDDuplicatedIPv6AddressFoundTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3801)
)
panIPV6NDDuplicatedIPv6AddressFoundTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panIPV6NDDuplicatedIPv6AddressFoundTrap.setStatus(
        "current"
    )

panIPV6NDInconsistentRaMessageReceivedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3802)
)
panIPV6NDInconsistentRaMessageReceivedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panIPV6NDInconsistentRaMessageReceivedTrap.setStatus(
        "current"
    )

panDYNAMICUPDATESPaloAltoNetworksMessageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3900)
)
panDYNAMICUPDATESPaloAltoNetworksMessageTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDYNAMICUPDATESPaloAltoNetworksMessageTrap.setStatus(
        "current"
    )

panUUIDPolicyRuleUuidModifiedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4000)
)
panUUIDPolicyRuleUuidModifiedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUUIDPolicyRuleUuidModifiedTrap.setStatus(
        "current"
    )

panGRETunnelStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4100)
)
panGRETunnelStatusUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGRETunnelStatusUpTrap.setStatus(
        "current"
    )

panGRETunnelStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4101)
)
panGRETunnelStatusDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGRETunnelStatusDownTrap.setStatus(
        "current"
    )

panGRETunnelRecurRoutingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4102)
)
panGRETunnelRecurRoutingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGRETunnelRecurRoutingTrap.setStatus(
        "current"
    )

panPANOCHECKPanoramaCheckSkipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4200)
)
panPANOCHECKPanoramaCheckSkipTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPANOCHECKPanoramaCheckSkipTrap.setStatus(
        "current"
    )

panPANOCHECKPanoramaCheckAutoDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4201)
)
panPANOCHECKPanoramaCheckAutoDisabledTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPANOCHECKPanoramaCheckAutoDisabledTrap.setStatus(
        "current"
    )

panPANOCHECKPanoramaCheckAutoRevertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4202)
)
panPANOCHECKPanoramaCheckAutoRevertTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPANOCHECKPanoramaCheckAutoRevertTrap.setStatus(
        "current"
    )

panPANOCHECKPanoramaCheckTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4203)
)
panPANOCHECKPanoramaCheckTestTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPANOCHECKPanoramaCheckTestTrap.setStatus(
        "current"
    )

panSDWANSdwanVifStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4300)
)
panSDWANSdwanVifStatusUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSDWANSdwanVifStatusUpTrap.setStatus(
        "current"
    )

panSDWANSdwanVifStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4301)
)
panSDWANSdwanVifStatusDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHostname"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSDWANSdwanVifStatusDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-TRAPS",
    **{"panTrapMibsModule": panTrapMibsModule,
       "panReceiveTime": panReceiveTime,
       "panSerial": panSerial,
       "panEventType": panEventType,
       "panEventSubType": panEventSubType,
       "panHost": panHost,
       "panVsys": panVsys,
       "panSeqno": panSeqno,
       "panActionflags": panActionflags,
       "panHostInetAddrType": panHostInetAddrType,
       "panHostInetAddr": panHostInetAddr,
       "panHostname": panHostname,
       "panSource": panSource,
       "panDestination": panDestination,
       "panNatSource": panNatSource,
       "panNatDestination": panNatDestination,
       "panRule": panRule,
       "panSrcUser": panSrcUser,
       "panDstUser": panDstUser,
       "panApplication": panApplication,
       "panSourceZone": panSourceZone,
       "panDestinationZone": panDestinationZone,
       "panIngressInterface": panIngressInterface,
       "panEgressInterface": panEgressInterface,
       "panLogForwardingProfile": panLogForwardingProfile,
       "panSessionID": panSessionID,
       "panRepeatCount": panRepeatCount,
       "panSourcePort": panSourcePort,
       "panDestinationPort": panDestinationPort,
       "panNatSourcePort": panNatSourcePort,
       "panNatDestinationPort": panNatDestinationPort,
       "panFlags": panFlags,
       "panProtocol": panProtocol,
       "panAction": panAction,
       "panTimeGenerated": panTimeGenerated,
       "panSrcloc": panSrcloc,
       "panDstloc": panDstloc,
       "panSourceInetAddrType": panSourceInetAddrType,
       "panSourceInetAddr": panSourceInetAddr,
       "panDestinationInetAddrType": panDestinationInetAddrType,
       "panDestinationInetAddr": panDestinationInetAddr,
       "panNatSourceInetAddrType": panNatSourceInetAddrType,
       "panNatSourceInetAddr": panNatSourceInetAddr,
       "panNatDestinationInetAddrType": panNatDestinationInetAddrType,
       "panNatDestinationInetAddr": panNatDestinationInetAddr,
       "panSourceUUID": panSourceUUID,
       "panDestinationUUID": panDestinationUUID,
       "panTunnel": panTunnel,
       "panRuleUUID": panRuleUUID,
       "panTrafficBytes": panTrafficBytes,
       "panTrafficPackets": panTrafficPackets,
       "panTrafficStartTime": panTrafficStartTime,
       "panTrafficElapsed": panTrafficElapsed,
       "panTrafficCategory": panTrafficCategory,
       "panTrafficSessionEndReason": panTrafficSessionEndReason,
       "panTrafficTunnelID": panTrafficTunnelID,
       "panTrafficImsi": panTrafficImsi,
       "panTrafficMonitorTag": panTrafficMonitorTag,
       "panTrafficImei": panTrafficImei,
       "panTrafficParentSessionId": panTrafficParentSessionId,
       "panTrafficParentStartTime": panTrafficParentStartTime,
       "panConfigCmd": panConfigCmd,
       "panConfigAdmin": panConfigAdmin,
       "panConfigClient": panConfigClient,
       "panConfigResult": panConfigResult,
       "panConfigPath": panConfigPath,
       "panThreatId": panThreatId,
       "panThreatCategory": panThreatCategory,
       "panThreatContentType": panThreatContentType,
       "panThreatSeverity": panThreatSeverity,
       "panThreatDirection": panThreatDirection,
       "panMiscellaneous": panMiscellaneous,
       "panPcapId": panPcapId,
       "panFileDigest": panFileDigest,
       "panCloud": panCloud,
       "panUrlIndex": panUrlIndex,
       "panUserAgent": panUserAgent,
       "panXff": panXff,
       "panReferer": panReferer,
       "panSender": panSender,
       "panSubject": panSubject,
       "panRecipient": panRecipient,
       "panFileType": panFileType,
       "panReportId": panReportId,
       "panHttpMethod": panHttpMethod,
       "panThreatTunnelID": panThreatTunnelID,
       "panThreatImsi": panThreatImsi,
       "panThreatMonitorTag": panThreatMonitorTag,
       "panThreatImei": panThreatImei,
       "panThreatParentSessionId": panThreatParentSessionId,
       "panThreatParentStartTime": panThreatParentStartTime,
       "panThrCategory": panThrCategory,
       "panHipSourceUser": panHipSourceUser,
       "panHipMachineName": panHipMachineName,
       "panHipSource": panHipSource,
       "panHipMatch": panHipMatch,
       "panHipMatchType": panHipMatchType,
       "panHipRepeatCount": panHipRepeatCount,
       "panHipOS": panHipOS,
       "panHipSourceInetAddrType": panHipSourceInetAddrType,
       "panHipSourceInetAddr": panHipSourceInetAddr,
       "panHipSourceIPv6": panHipSourceIPv6,
       "panHipSourceIPv6InetAddrType": panHipSourceIPv6InetAddrType,
       "panHipSourceIPv6InetAddr": panHipSourceIPv6InetAddr,
       "panSystemEventId": panSystemEventId,
       "panSystemObject": panSystemObject,
       "panSystemModule": panSystemModule,
       "panSystemSeverity": panSystemSeverity,
       "panSystemDescription": panSystemDescription,
       "panCorrDG1": panCorrDG1,
       "panCorrDG2": panCorrDG2,
       "panCorrDG3": panCorrDG3,
       "panCorrDG4": panCorrDG4,
       "panCorrObjName": panCorrObjName,
       "panCorrObjID": panCorrObjID,
       "panCorrSeverity": panCorrSeverity,
       "panCorrEvidence": panCorrEvidence,
       "panGtpTunnelID": panGtpTunnelID,
       "panGtpImsi": panGtpImsi,
       "panGtpMonitorTag": panGtpMonitorTag,
       "panGtpImei": panGtpImei,
       "panGtpParentSessionId": panGtpParentSessionId,
       "panGtpParentStartTime": panGtpParentStartTime,
       "panGtpMsisdn": panGtpMsisdn,
       "panGtpApn": panGtpApn,
       "panGtpRat": panGtpRat,
       "panGtpMsgType": panGtpMsgType,
       "panGtpEndipaddrInetAddrType": panGtpEndipaddrInetAddrType,
       "panGtpEndIpAddr": panGtpEndIpAddr,
       "panGtpTeid1": panGtpTeid1,
       "panGtpTeid2": panGtpTeid2,
       "panGtpInterface": panGtpInterface,
       "panGtpCauseCode": panGtpCauseCode,
       "panGtpEventType": panGtpEventType,
       "panGtpSeverity": panGtpSeverity,
       "panGtpMcc": panGtpMcc,
       "panGtpMnc": panGtpMnc,
       "panGtpAreaCode": panGtpAreaCode,
       "panGtpCellId": panGtpCellId,
       "panGtpEventCode": panGtpEventCode,
       "panGtpBytes": panGtpBytes,
       "panGtpPackets": panGtpPackets,
       "panGtpMaxEncap": panGtpMaxEncap,
       "panGtpUnknownProto": panGtpUnknownProto,
       "panGtpStrictCheck": panGtpStrictCheck,
       "panGtpTunnelFragment": panGtpTunnelFragment,
       "panGtpSessionsCreated": panGtpSessionsCreated,
       "panGtpSessionsClosed": panGtpSessionsClosed,
       "panGtpSessionEndReason": panGtpSessionEndReason,
       "panGtpActionSource": panGtpActionSource,
       "panGtpStartTime": panGtpStartTime,
       "panGtpElapsed": panGtpElapsed,
       "panGtpTCIRule": panGtpTCIRule,
       "panGtpRemoteUserIpInetAddrType": panGtpRemoteUserIpInetAddrType,
       "panGtpRemoteUserIp": panGtpRemoteUserIp,
       "panGtpRemoteUserId": panGtpRemoteUserId,
       "panUseridSourceInetAddrType": panUseridSourceInetAddrType,
       "panUseridSourceInetAddr": panUseridSourceInetAddr,
       "panUseridUser": panUseridUser,
       "panUseridDataSourceName": panUseridDataSourceName,
       "panUseridEventID": panUseridEventID,
       "panUseridRepeatCount": panUseridRepeatCount,
       "panUseridTimeout": panUseridTimeout,
       "panUseridBeginport": panUseridBeginport,
       "panUseridEndport": panUseridEndport,
       "panUseridDataSource": panUseridDataSource,
       "panUseridDataSourceType": panUseridDataSourceType,
       "panUseridFactorType": panUseridFactorType,
       "panUseridFactorTime": panUseridFactorTime,
       "panUseridFactorNo": panUseridFactorNo,
       "panAuthSourceInetAddrType": panAuthSourceInetAddrType,
       "panAuthSourceInetAddr": panAuthSourceInetAddr,
       "panAuthUser": panAuthUser,
       "panAuthNormalizeUser": panAuthNormalizeUser,
       "panAuthObject": panAuthObject,
       "panAuthPolicy": panAuthPolicy,
       "panAuthRepeatCount": panAuthRepeatCount,
       "panAuthID": panAuthID,
       "panAuthVendor": panAuthVendor,
       "panAuthLogForwardingProfile": panAuthLogForwardingProfile,
       "panAuthClientType": panAuthClientType,
       "panAuthDescription": panAuthDescription,
       "panAuthServerProfile": panAuthServerProfile,
       "panAuthEvent": panAuthEvent,
       "panAuthFactorNo": panAuthFactorNo,
       "panAuthProto": panAuthProto,
       "panSctpAssocId": panSctpAssocId,
       "panSctpPpid": panSctpPpid,
       "panSctpSeverity": panSctpSeverity,
       "panSctpChunkType": panSctpChunkType,
       "panSctpEventType": panSctpEventType,
       "panSctpEventCode": panSctpEventCode,
       "panSctpVerifTag1": panSctpVerifTag1,
       "panSctpVerifTag2": panSctpVerifTag2,
       "panSctpCauseCode": panSctpCauseCode,
       "panSctpDiamAppId": panSctpDiamAppId,
       "panSctpDiamCmdCode": panSctpDiamCmdCode,
       "panSctpDiamAvpCode": panSctpDiamAvpCode,
       "panSctpStreamId": panSctpStreamId,
       "panSctpOpCode": panSctpOpCode,
       "panSctpCallingSSN": panSctpCallingSSN,
       "panSctpCallingGT": panSctpCallingGT,
       "panSctpEndReason": panSctpEndReason,
       "panSctpChunks": panSctpChunks,
       "panSctpPackets": panSctpPackets,
       "panIpTagIp": panIpTagIp,
       "panIpTagName": panIpTagName,
       "panIpTagEvent": panIpTagEvent,
       "panIpTagRepeatCount": panIpTagRepeatCount,
       "panIpTagTimeout": panIpTagTimeout,
       "panIpTagDataSourceName": panIpTagDataSourceName,
       "panIpTagDataSourceType": panIpTagDataSourceType,
       "panIpTagDataSourceSubType": panIpTagDataSourceSubType,
       "panGlobalProtectStatus": panGlobalProtectStatus,
       "panGlobalProtectStage": panGlobalProtectStage,
       "panGlobalProtectAuthMethod": panGlobalProtectAuthMethod,
       "panGlobalProtectTunnelType": panGlobalProtectTunnelType,
       "panGlobalProtectPortal": panGlobalProtectPortal,
       "panGlobalProtectSrcRegion": panGlobalProtectSrcRegion,
       "panGlobalProtectPublicIP": panGlobalProtectPublicIP,
       "panGlobalProtectPublicIPv6": panGlobalProtectPublicIPv6,
       "panGlobalProtectPrivateIP": panGlobalProtectPrivateIP,
       "panGlobalProtectPrivateIPv6": panGlobalProtectPrivateIPv6,
       "panGlobalProtectClientVersion": panGlobalProtectClientVersion,
       "panGlobalProtectClientOSVersion": panGlobalProtectClientOSVersion,
       "panGlobalProtectLoginDuration": panGlobalProtectLoginDuration,
       "panGlobalProtectConnectMethod": panGlobalProtectConnectMethod,
       "panGlobalProtectReason": panGlobalProtectReason,
       "panGlobalProtectLocation": panGlobalProtectLocation,
       "panGlobalProtectErrorCode": panGlobalProtectErrorCode,
       "panGlobalProtectError": panGlobalProtectError,
       "panConfigTrap": panConfigTrap,
       "panTrafficTrap": panTrafficTrap,
       "panThreatTrap": panThreatTrap,
       "panHipMatchTrap": panHipMatchTrap,
       "panGtpTrap": panGtpTrap,
       "panUseridTrap": panUseridTrap,
       "panAuthTrap": panAuthTrap,
       "panSctpTrap": panSctpTrap,
       "panCorrTrap": panCorrTrap,
       "panIpTagTrap": panIpTagTrap,
       "panGlobalprotectTrap": panGlobalprotectTrap,
       "panCryptoCertExpiryTrap": panCryptoCertExpiryTrap,
       "panCryptoMkeyExpiryTrap": panCryptoMkeyExpiryTrap,
       "panCryptoMkeyExpiryReminderTrap": panCryptoMkeyExpiryReminderTrap,
       "panCryptoHSMStateChangeTrap": panCryptoHSMStateChangeTrap,
       "panCryptoPrivateKeyExportTrap": panCryptoPrivateKeyExportTrap,
       "panCryptoDeployMkeyChangeTrap": panCryptoDeployMkeyChangeTrap,
       "panCryptoMkeyChangeTrap": panCryptoMkeyChangeTrap,
       "panDHCPLeaseStartTrap": panDHCPLeaseStartTrap,
       "panDHCPLeaseEndTrap": panDHCPLeaseEndTrap,
       "panDHCPServerOnTrap": panDHCPServerOnTrap,
       "panDHCPServerAutoProbeOnTrap": panDHCPServerAutoProbeOnTrap,
       "panDHCPServerAutoProbeOffTrap": panDHCPServerAutoProbeOffTrap,
       "panDHCPServerNoFreeIpTrap": panDHCPServerNoFreeIpTrap,
       "panDHCPIpAlreadyInUseTrap": panDHCPIpAlreadyInUseTrap,
       "panDHCPRelayOnTrap": panDHCPRelayOnTrap,
       "panDHCPRelayOffTrap": panDHCPRelayOffTrap,
       "panDHCPRelay6OnTrap": panDHCPRelay6OnTrap,
       "panDHCPRelay6OffTrap": panDHCPRelay6OffTrap,
       "panDHCPIfUpdateFailTrap": panDHCPIfUpdateFailTrap,
       "panDHCPIfUpdateOkTrap": panDHCPIfUpdateOkTrap,
       "panDHCPIfClearTrap": panDHCPIfClearTrap,
       "panDHCPIfRenewTriggerTrap": panDHCPIfRenewTriggerTrap,
       "panDHCPIfReleaseTriggerTrap": panDHCPIfReleaseTriggerTrap,
       "panDHCPIfRcvNakTrap": panDHCPIfRcvNakTrap,
       "panDHCPIfInheritTrap": panDHCPIfInheritTrap,
       "panDHCPIfDuplicateIpIntfTrap": panDHCPIfDuplicateIpIntfTrap,
       "panDHCPIfDuplicateIpRemoteTrap": panDHCPIfDuplicateIpRemoteTrap,
       "panDNSProxyCacheClearedTrap": panDNSProxyCacheClearedTrap,
       "panDNSProxyResolveFailTrap": panDNSProxyResolveFailTrap,
       "panDNSProxyObjectEnableTrap": panDNSProxyObjectEnableTrap,
       "panDNSProxyIfAddTrap": panDNSProxyIfAddTrap,
       "panDNSProxyIfDelTrap": panDNSProxyIfDelTrap,
       "panDNSProxyIfInheritTrap": panDNSProxyIfInheritTrap,
       "panDOSDosRuleChangedTrap": panDOSDosRuleChangedTrap,
       "panGeneralGeneralTrap": panGeneralGeneralTrap,
       "panGeneralSystemStartTrap": panGeneralSystemStartTrap,
       "panGeneralSystemShutdownTrap": panGeneralSystemShutdownTrap,
       "panGeneralAuthFailTrap": panGeneralAuthFailTrap,
       "panGeneralAuthSuccessTrap": panGeneralAuthSuccessTrap,
       "panGeneralTacLoginTrap": panGeneralTacLoginTrap,
       "panGeneralAuthServerDownTrap": panGeneralAuthServerDownTrap,
       "panGeneralAdminDiscardTrap": panGeneralAdminDiscardTrap,
       "panGeneralBootstrapFailureTrap": panGeneralBootstrapFailureTrap,
       "panGlobalprotectgatewayRegistSuccTrap": panGlobalprotectgatewayRegistSuccTrap,
       "panGlobalprotectgatewayRegistFailTrap": panGlobalprotectgatewayRegistFailTrap,
       "panGlobalprotectgatewayLogoutSuccTrap": panGlobalprotectgatewayLogoutSuccTrap,
       "panGlobalprotectgatewayLogoutFailTrap": panGlobalprotectgatewayLogoutFailTrap,
       "panGlobalProtectGatewayConfigSuccTrap": panGlobalProtectGatewayConfigSuccTrap,
       "panGlobalProtectGatewayConfigFailTrap": panGlobalProtectGatewayConfigFailTrap,
       "panGlobalProtectGatewayConfigReleaseTrap": panGlobalProtectGatewayConfigReleaseTrap,
       "panGlobalProtectGatewaySwitchSuccTrap": panGlobalProtectGatewaySwitchSuccTrap,
       "panGlobalProtectGatewaySwitchFailTrap": panGlobalProtectGatewaySwitchFailTrap,
       "panGlobalProtectGatewayAuthSuccTrap": panGlobalProtectGatewayAuthSuccTrap,
       "panGlobalProtectGatewayAuthFailTrap": panGlobalProtectGatewayAuthFailTrap,
       "panGlobalProtectGatewayAgentMsgTrap": panGlobalProtectGatewayAgentMsgTrap,
       "panGlobalProtectGatewayInvalidLicenseTrap": panGlobalProtectGatewayInvalidLicenseTrap,
       "panGlobalProtectGatewayInheritanceTrap": panGlobalProtectGatewayInheritanceTrap,
       "panGlobalProtectPortalConfigSuccTrap": panGlobalProtectPortalConfigSuccTrap,
       "panGlobalProtectPortalConfigFailTrap": panGlobalProtectPortalConfigFailTrap,
       "panGlobalProtectPortalAuthSuccTrap": panGlobalProtectPortalAuthSuccTrap,
       "panGlobalProtectPortalAuthFailTrap": panGlobalProtectPortalAuthFailTrap,
       "panGlobalprotectgatewaySatauthSuccTrap": panGlobalprotectgatewaySatauthSuccTrap,
       "panGlobalprotectgatewaySatauthFailTrap": panGlobalprotectgatewaySatauthFailTrap,
       "panGlobalprotectgatewayRouteAddFailTrap": panGlobalprotectgatewayRouteAddFailTrap,
       "panGlobalprotectgatewayRouteResetFailTrap": panGlobalprotectgatewayRouteResetFailTrap,
       "panGlobalprotectgatewayTunUpTrap": panGlobalprotectgatewayTunUpTrap,
       "panGlobalprotectgatewayTunDownTrap": panGlobalprotectgatewayTunDownTrap,
       "panGlobalprotectgatewayDupSubnetsTrap": panGlobalprotectgatewayDupSubnetsTrap,
       "panGlobalprotectgatewayDeniedRoutesTrap": panGlobalprotectgatewayDeniedRoutesTrap,
       "panGlobalprotectgatewayTunMonDownTrap": panGlobalprotectgatewayTunMonDownTrap,
       "panGlobalprotectgatewayTunMonUpTrap": panGlobalprotectgatewayTunMonUpTrap,
       "panGlobalprotectportalSatconfigSuccTrap": panGlobalprotectportalSatconfigSuccTrap,
       "panGlobalprotectportalSatconfigFailTrap": panGlobalprotectportalSatconfigFailTrap,
       "panGlobalprotectportalSatauthSuccTrap": panGlobalprotectportalSatauthSuccTrap,
       "panGlobalprotectportalSatauthFailTrap": panGlobalprotectportalSatauthFailTrap,
       "panGlobalprotectportalSatcertSuccTrap": panGlobalprotectportalSatcertSuccTrap,
       "panGlobalprotectportalSatcertFailTrap": panGlobalprotectportalSatcertFailTrap,
       "panGlobalprotectgatewayTunHardlifetimeExpiredTrap": panGlobalprotectgatewayTunHardlifetimeExpiredTrap,
       "panGlobalprotectgatewayTunDpInstallErrTrap": panGlobalprotectgatewayTunDpInstallErrTrap,
       "panGlobalprotectportalGenportalcookieSuccTrap": panGlobalprotectportalGenportalcookieSuccTrap,
       "panGlobalprotectportalGenportalcookieFailTrap": panGlobalprotectportalGenportalcookieFailTrap,
       "panGlobalprotectgatewayFramedIpSuccTrap": panGlobalprotectgatewayFramedIpSuccTrap,
       "panGlobalprotectgatewayFramedIpFailTrap": panGlobalprotectgatewayFramedIpFailTrap,
       "panGlobalprotectgatewayGencookieSuccTrap": panGlobalprotectgatewayGencookieSuccTrap,
       "panGlobalprotectgatewayGencookieFailTrap": panGlobalprotectgatewayGencookieFailTrap,
       "panGlobalprotectgatewayFramedIpv6SuccTrap": panGlobalprotectgatewayFramedIpv6SuccTrap,
       "panGlobalprotectgatewayFramedIpv6FailTrap": panGlobalprotectgatewayFramedIpv6FailTrap,
       "panGlobalprotectportalLogoutSuccTrap": panGlobalprotectportalLogoutSuccTrap,
       "panGlobalprotectportalLogoutFailTrap": panGlobalprotectportalLogoutFailTrap,
       "panHAPreemptTrap": panHAPreemptTrap,
       "panHAStateChangeTrap": panHAStateChangeTrap,
       "panHAStateOverrideTrap": panHAStateOverrideTrap,
       "panHADataplaneDownTrap": panHADataplaneDownTrap,
       "panHAPolicyPushFailTrap": panHAPolicyPushFailTrap,
       "panHAHa1LinkChangeTrap": panHAHa1LinkChangeTrap,
       "panHAHa2LinkChangeTrap": panHAHa2LinkChangeTrap,
       "panHAConnectChangeTrap": panHAConnectChangeTrap,
       "panHAPathMonitorDownTrap": panHAPathMonitorDownTrap,
       "panHALinkMonitorDownTrap": panHALinkMonitorDownTrap,
       "panHAHa3LinkChangeTrap": panHAHa3LinkChangeTrap,
       "panHAPathMonitorUpTrap": panHAPathMonitorUpTrap,
       "panHALinkMonitorUpTrap": panHALinkMonitorUpTrap,
       "panHAPeerSyncFailureTrap": panHAPeerSyncFailureTrap,
       "panHAConfigFailureTrap": panHAConfigFailureTrap,
       "panHAConfigNotSynchTrap": panHAConfigNotSynchTrap,
       "panHAPeerErrorTrap": panHAPeerErrorTrap,
       "panHAPre13Trap": panHAPre13Trap,
       "panHAPre20Trap": panHAPre20Trap,
       "panHAPeerVersionMatchTrap": panHAPeerVersionMatchTrap,
       "panHAPeerVersionSupportedTrap": panHAPeerVersionSupportedTrap,
       "panHAPeerVersionUnsupportedTrap": panHAPeerVersionUnsupportedTrap,
       "panHAPeerVersionDegradedTrap": panHAPeerVersionDegradedTrap,
       "panHAPeerCompatMismatchTrap": panHAPeerCompatMismatchTrap,
       "panHAPeerCompatMatchTrap": panHAPeerCompatMatchTrap,
       "panHAPeerCompatFailTrap": panHAPeerCompatFailTrap,
       "panHAPeerSplitBrainTrap": panHAPeerSplitBrainTrap,
       "panHASplitBrainTrap": panHASplitBrainTrap,
       "panHAPreemptLoopTrap": panHAPreemptLoopTrap,
       "panHANonFunctionalLoopTrap": panHANonFunctionalLoopTrap,
       "panHAPeerShutdownTrap": panHAPeerShutdownTrap,
       "panHANfsPanlogsFailTrap": panHANfsPanlogsFailTrap,
       "panHAInternalHaErrorTrap": panHAInternalHaErrorTrap,
       "panHASystemFailureTrap": panHASystemFailureTrap,
       "panHAHa2KeepAliveTrap": panHAHa2KeepAliveTrap,
       "panHASlotFailureTrap": panHASlotFailureTrap,
       "panHASlotMismatchTrap": panHASlotMismatchTrap,
       "panHASlotControlFailureTrap": panHASlotControlFailureTrap,
       "panHASlotControlEventTrap": panHASlotControlEventTrap,
       "panHASessionSynchTrap": panHASessionSynchTrap,
       "panHAVmAwsInterfaceTrap": panHAVmAwsInterfaceTrap,
       "panHWDiskErrorsTrap": panHWDiskErrorsTrap,
       "panHWSlotUpTrap": panHWSlotUpTrap,
       "panHWInsufficientPowerTrap": panHWInsufficientPowerTrap,
       "panHWSlotUnsupportedTrap": panHWSlotUnsupportedTrap,
       "panHWSlotStartingTrap": panHWSlotStartingTrap,
       "panHWSlotStoppingTrap": panHWSlotStoppingTrap,
       "panHWSlotFailureTrap": panHWSlotFailureTrap,
       "panHWSlotPoweroffTrap": panHWSlotPoweroffTrap,
       "panHWSlotAdminpoweroffTrap": panHWSlotAdminpoweroffTrap,
       "panHWSlotInsertedTrap": panHWSlotInsertedTrap,
       "panHWSlotRemovedTrap": panHWSlotRemovedTrap,
       "panHWPsInsertedTrap": panHWPsInsertedTrap,
       "panHWPsRemovedTrap": panHWPsRemovedTrap,
       "panHWPsFailureTrap": panHWPsFailureTrap,
       "panHWFanInsertedTrap": panHWFanInsertedTrap,
       "panHWFanRemovedTrap": panHWFanRemovedTrap,
       "panHWFanFailureTrap": panHWFanFailureTrap,
       "panHWBootstrapImageErrorTrap": panHWBootstrapImageErrorTrap,
       "panHWBootstrapConfigNotFoundTrap": panHWBootstrapConfigNotFoundTrap,
       "panHWBadParamsBootstrapConfigTrap": panHWBadParamsBootstrapConfigTrap,
       "panHWMediaSanityFailureTrap": panHWMediaSanityFailureTrap,
       "panHWUsbMediaPrepSuccessTrap": panHWUsbMediaPrepSuccessTrap,
       "panHWBootstrapSuccessTrap": panHWBootstrapSuccessTrap,
       "panHWBootstrapLicenseFailureTrap": panHWBootstrapLicenseFailureTrap,
       "panHWBootstrapContentFailureTrap": panHWBootstrapContentFailureTrap,
       "panHWBootstrapMediaDetectTrap": panHWBootstrapMediaDetectTrap,
       "panHWBootstrapMediaSanityTrap": panHWBootstrapMediaSanityTrap,
       "panHWBootstrapImageUpgradeTrap": panHWBootstrapImageUpgradeTrap,
       "panHWBootstrapOpCmdTrap": panHWBootstrapOpCmdTrap,
       "panNTDPRestartTrap": panNTDPRestartTrap,
       "panNTDPTimeLearnTrap": panNTDPTimeLearnTrap,
       "panNTDPSyncTrap": panNTDPSyncTrap,
       "panNTDPAuthTrap": panNTDPAuthTrap,
       "panPBFNhUpTrap": panPBFNhUpTrap,
       "panPBFNhDownTrap": panPBFNhDownTrap,
       "panPORTLinkChangeTrap": panPORTLinkChangeTrap,
       "panPORTNonqualSfpTrap": panPORTNonqualSfpTrap,
       "panPORTNonqualSfpPlusTrap": panPORTNonqualSfpPlusTrap,
       "panPORTNonqualXfpTrap": panPORTNonqualXfpTrap,
       "panPORTNonsuppForcedTrap": panPORTNonsuppForcedTrap,
       "panPORTInvalidModuleTrap": panPORTInvalidModuleTrap,
       "panPORTSdwanLinkChangeTrap": panPORTSdwanLinkChangeTrap,
       "panPPPOEInitiateTrap": panPPPOEInitiateTrap,
       "panPPPOEConnectTrap": panPPPOEConnectTrap,
       "panPPPOEConnectFailTrap": panPPPOEConnectFailTrap,
       "panPPPOETerminateTrap": panPPPOETerminateTrap,
       "panPPPOEIfUpdateFailTrap": panPPPOEIfUpdateFailTrap,
       "panRASRasmgrConfigP1SuccessTrap": panRASRasmgrConfigP1SuccessTrap,
       "panRASRasmgrConfigP1FailedTrap": panRASRasmgrConfigP1FailedTrap,
       "panRASRasmgrConfigP1AbortTrap": panRASRasmgrConfigP1AbortTrap,
       "panRASRasmgrConfigP2SuccessTrap": panRASRasmgrConfigP2SuccessTrap,
       "panRASRasmgrConfigP2FailedTrap": panRASRasmgrConfigP2FailedTrap,
       "panRASRasmgrDaemonStartTrap": panRASRasmgrDaemonStartTrap,
       "panRASRasmgrDaemonExitTrap": panRASRasmgrDaemonExitTrap,
       "panRASRasmgrDaemonInitTrap": panRASRasmgrDaemonInitTrap,
       "panRASRasmgrFlowFullSyncStartTrap": panRASRasmgrFlowFullSyncStartTrap,
       "panRASRasmgrFlowFullSyncAbortTrap": panRASRasmgrFlowFullSyncAbortTrap,
       "panRASRasmgrFlowFullSyncDoneTrap": panRASRasmgrFlowFullSyncDoneTrap,
       "panRASRasmgrHaFullSyncStartTrap": panRASRasmgrHaFullSyncStartTrap,
       "panRASRasmgrHaFullSyncAbortTrap": panRASRasmgrHaFullSyncAbortTrap,
       "panRASRasmgrHaFullSyncDoneTrap": panRASRasmgrHaFullSyncDoneTrap,
       "panROUTINGRoutedConfigP1SuccessTrap": panROUTINGRoutedConfigP1SuccessTrap,
       "panROUTINGRoutedConfigP1FailedTrap": panROUTINGRoutedConfigP1FailedTrap,
       "panROUTINGRoutedConfigP1AbortTrap": panROUTINGRoutedConfigP1AbortTrap,
       "panROUTINGRoutedConfigP2SuccessTrap": panROUTINGRoutedConfigP2SuccessTrap,
       "panROUTINGRoutedConfigP2FailedTrap": panROUTINGRoutedConfigP2FailedTrap,
       "panROUTINGRoutedDaemonStartTrap": panROUTINGRoutedDaemonStartTrap,
       "panROUTINGRoutedDaemonExitTrap": panROUTINGRoutedDaemonExitTrap,
       "panROUTINGRoutedDaemonInitTrap": panROUTINGRoutedDaemonInitTrap,
       "panROUTINGRoutedFibSyncPeerBackupTrap": panROUTINGRoutedFibSyncPeerBackupTrap,
       "panROUTINGRoutedFibSyncSelfMasterTrap": panROUTINGRoutedFibSyncSelfMasterTrap,
       "panROUTINGRoutedRTMBadRouteTrap": panROUTINGRoutedRTMBadRouteTrap,
       "panROUTINGRoutedOSPFLSAChksumFailedTrap": panROUTINGRoutedOSPFLSAChksumFailedTrap,
       "panROUTINGRoutedOSPFLSAChksumInvalidTrap": panROUTINGRoutedOSPFLSAChksumInvalidTrap,
       "panROUTINGRoutedOSPFAuthtypeBadTrap": panROUTINGRoutedOSPFAuthtypeBadTrap,
       "panROUTINGRoutedOSPFPasswordBadTrap": panROUTINGRoutedOSPFPasswordBadTrap,
       "panROUTINGRoutedOSPFChksumBadTrap": panROUTINGRoutedOSPFChksumBadTrap,
       "panROUTINGRoutedOSPFSequenceBadTrap": panROUTINGRoutedOSPFSequenceBadTrap,
       "panROUTINGRoutedOSPFMd5chksumBadTrap": panROUTINGRoutedOSPFMd5chksumBadTrap,
       "panROUTINGRoutedOSPFMd5lengthBadTrap": panROUTINGRoutedOSPFMd5lengthBadTrap,
       "panROUTINGRoutedOSPFHelloHelloIntvalBadTrap": panROUTINGRoutedOSPFHelloHelloIntvalBadTrap,
       "panROUTINGRoutedOSPFHelloDeadIntvalBadTrap": panROUTINGRoutedOSPFHelloDeadIntvalBadTrap,
       "panROUTINGRoutedOSPFHelloNetmaskBadTrap": panROUTINGRoutedOSPFHelloNetmaskBadTrap,
       "panROUTINGRoutedOSPFHelloAreaTypeBadTrap": panROUTINGRoutedOSPFHelloAreaTypeBadTrap,
       "panROUTINGRoutedOSPFNeighbor2dirTrap": panROUTINGRoutedOSPFNeighbor2dirTrap,
       "panROUTINGRoutedOSPFNeighborFullTrap": panROUTINGRoutedOSPFNeighborFullTrap,
       "panROUTINGRoutedOSPFNeighborDownTrap": panROUTINGRoutedOSPFNeighborDownTrap,
       "panROUTINGRoutedRIPPeerAddTrap": panROUTINGRoutedRIPPeerAddTrap,
       "panROUTINGRoutedRIPPeerDelTrap": panROUTINGRoutedRIPPeerDelTrap,
       "panROUTINGRoutedRIPAuthtypeBadTrap": panROUTINGRoutedRIPAuthtypeBadTrap,
       "panROUTINGRoutedRIPAuthFailedTrap": panROUTINGRoutedRIPAuthFailedTrap,
       "panROUTINGRoutedRIPMd5lengthBadTrap": panROUTINGRoutedRIPMd5lengthBadTrap,
       "panROUTINGRoutedBGPPeerEnterEstablishedTrap": panROUTINGRoutedBGPPeerEnterEstablishedTrap,
       "panROUTINGRoutedBGPPeerLeftEstablishedTrap": panROUTINGRoutedBGPPeerLeftEstablishedTrap,
       "panROUTINGRoutedBGPPeerFailedTrap": panROUTINGRoutedBGPPeerFailedTrap,
       "panROUTINGRoutedBGPPeerRestartedTrap": panROUTINGRoutedBGPPeerRestartedTrap,
       "panROUTINGRoutedBGPPeerRestartFailedTrap": panROUTINGRoutedBGPPeerRestartFailedTrap,
       "panROUTINGRoutedBGPRefreshSentTrap": panROUTINGRoutedBGPRefreshSentTrap,
       "panROUTINGRoutedBGPRibinRecalcTrap": panROUTINGRoutedBGPRibinRecalcTrap,
       "panROUTINGRoutedPIMInterfaceStateChangedTrap": panROUTINGRoutedPIMInterfaceStateChangedTrap,
       "panROUTINGRoutedPIMNewDrElectedTrap": panROUTINGRoutedPIMNewDrElectedTrap,
       "panROUTINGRoutedPIMNeighborDiscoveredTrap": panROUTINGRoutedPIMNeighborDiscoveredTrap,
       "panROUTINGRoutedPIMNeighborDisappearedTrap": panROUTINGRoutedPIMNeighborDisappearedTrap,
       "panROUTINGRoutedIGMPWrongVersionTrap": panROUTINGRoutedIGMPWrongVersionTrap,
       "panROUTINGRoutedGenericEventTrap": panROUTINGRoutedGenericEventTrap,
       "panROUTINGRoutedOSPFStartGracefulRestartTrap": panROUTINGRoutedOSPFStartGracefulRestartTrap,
       "panROUTINGRoutedOSPFStoppedGracefulRestartTrap": panROUTINGRoutedOSPFStoppedGracefulRestartTrap,
       "panROUTINGRoutedOSPFStartHelperNodeTrap": panROUTINGRoutedOSPFStartHelperNodeTrap,
       "panROUTINGRoutedOSPFStopHelperModeTrap": panROUTINGRoutedOSPFStopHelperModeTrap,
       "panROUTINGRoutedOSPFNotHelpTrap": panROUTINGRoutedOSPFNotHelpTrap,
       "panROUTINGRoutedECMPTrap": panROUTINGRoutedECMPTrap,
       "panROUTINGRoutedBGPPeerMpExtensionNegotiateTrap": panROUTINGRoutedBGPPeerMpExtensionNegotiateTrap,
       "panROUTINGPathMonitorFailureTrap": panROUTINGPathMonitorFailureTrap,
       "panROUTINGPathMonitorRecoveryTrap": panROUTINGPathMonitorRecoveryTrap,
       "panSSLVPNSslvpnRegistSuccTrap": panSSLVPNSslvpnRegistSuccTrap,
       "panSSLVPNSslvpnRegistFailTrap": panSSLVPNSslvpnRegistFailTrap,
       "panSSLVPNSslvpnLogoutSuccTrap": panSSLVPNSslvpnLogoutSuccTrap,
       "panSSLVPNSslvpnLogoutFailTrap": panSSLVPNSslvpnLogoutFailTrap,
       "panSSLVPNSslvpnConfigSuccTrap": panSSLVPNSslvpnConfigSuccTrap,
       "panSSLVPNSslvpnConfigFailTrap": panSSLVPNSslvpnConfigFailTrap,
       "panSSLVPNSslvpnConfigReleaseTrap": panSSLVPNSslvpnConfigReleaseTrap,
       "panSSLVPNSslvpnSwitchSuccTrap": panSSLVPNSslvpnSwitchSuccTrap,
       "panSSLVPNSslvpnSwitchFailTrap": panSSLVPNSslvpnSwitchFailTrap,
       "panSSLVPNSslvpnAuthSuccTrap": panSSLVPNSslvpnAuthSuccTrap,
       "panSSLVPNSslvpnAuthFailTrap": panSSLVPNSslvpnAuthFailTrap,
       "panVPNIkeConfigP1SuccessTrap": panVPNIkeConfigP1SuccessTrap,
       "panVPNIkeConfigP1FailedTrap": panVPNIkeConfigP1FailedTrap,
       "panVPNIkeConfigP1AbortTrap": panVPNIkeConfigP1AbortTrap,
       "panVPNIkeConfigP2SuccessTrap": panVPNIkeConfigP2SuccessTrap,
       "panVPNIkeConfigP2FailedTrap": panVPNIkeConfigP2FailedTrap,
       "panVPNIkeDaemonStartTrap": panVPNIkeDaemonStartTrap,
       "panVPNIkeDaemonExitTrap": panVPNIkeDaemonExitTrap,
       "panVPNIkeDaemonInitTrap": panVPNIkeDaemonInitTrap,
       "panVPNIkeNegoP1StartTrap": panVPNIkeNegoP1StartTrap,
       "panVPNIkeNegoP1FailTrap": panVPNIkeNegoP1FailTrap,
       "panVPNIkeNegoP1SuccTrap": panVPNIkeNegoP1SuccTrap,
       "panVPNIkeNegoP1ExpireTrap": panVPNIkeNegoP1ExpireTrap,
       "panVPNIkeNegoP1DeleteTrap": panVPNIkeNegoP1DeleteTrap,
       "panVPNIkeNegoP1DpdDnTrap": panVPNIkeNegoP1DpdDnTrap,
       "panVPNIkeNegoP1PskIdtypeTrap": panVPNIkeNegoP1PskIdtypeTrap,
       "panVPNIkeNegoP1FailPskTrap": panVPNIkeNegoP1FailPskTrap,
       "panVPNIkeNegoP1FailCommonTrap": panVPNIkeNegoP1FailCommonTrap,
       "panVPNIkeNegoP2StartTrap": panVPNIkeNegoP2StartTrap,
       "panVPNIkeNegoP2FailTrap": panVPNIkeNegoP2FailTrap,
       "panVPNIkeNegoP2SuccTrap": panVPNIkeNegoP2SuccTrap,
       "panVPNIkeNegoP2StaleP1Trap": panVPNIkeNegoP2StaleP1Trap,
       "panVPNIkeNegoP2DupRekeyTrap": panVPNIkeNegoP2DupRekeyTrap,
       "panVPNIkeNegoP2SimulContTrap": panVPNIkeNegoP2SimulContTrap,
       "panVPNIkeNegoP2SimulFailTrap": panVPNIkeNegoP2SimulFailTrap,
       "panVPNIkeNegoP2SimulDelayTrap": panVPNIkeNegoP2SimulDelayTrap,
       "panVPNIkeNegoP2NoP1Trap": panVPNIkeNegoP2NoP1Trap,
       "panVPNIkeNegoP2P1NotReadyTrap": panVPNIkeNegoP2P1NotReadyTrap,
       "panVPNIkeNegoP2ProxyIdBadTrap": panVPNIkeNegoP2ProxyIdBadTrap,
       "panVPNIkeNegoP2ProposalBadTrap": panVPNIkeNegoP2ProposalBadTrap,
       "panVPNIpsecKeyInstallTrap": panVPNIpsecKeyInstallTrap,
       "panVPNIpsecKeyDeleteTrap": panVPNIpsecKeyDeleteTrap,
       "panVPNIpsecKeyExpireTrap": panVPNIpsecKeyExpireTrap,
       "panVPNIkeRecvNotifyTrap": panVPNIkeRecvNotifyTrap,
       "panVPNIkeRecvP1DeleteTrap": panVPNIkeRecvP1DeleteTrap,
       "panVPNIkeRecvP2DeleteTrap": panVPNIkeRecvP2DeleteTrap,
       "panVPNIkeSendNotifyTrap": panVPNIkeSendNotifyTrap,
       "panVPNIkeSendP1DeleteTrap": panVPNIkeSendP1DeleteTrap,
       "panVPNIkeSendP2DeleteTrap": panVPNIkeSendP2DeleteTrap,
       "panVPNIkev2NegoIkeStartTrap": panVPNIkev2NegoIkeStartTrap,
       "panVPNIkev2NegoIkeFailTrap": panVPNIkev2NegoIkeFailTrap,
       "panVPNIkev2NegoIkeSuccTrap": panVPNIkev2NegoIkeSuccTrap,
       "panVPNIkev2NegoIkeExpireTrap": panVPNIkev2NegoIkeExpireTrap,
       "panVPNIkev2NegoIkeDeleteTrap": panVPNIkev2NegoIkeDeleteTrap,
       "panVPNIkev2NegoChildStartTrap": panVPNIkev2NegoChildStartTrap,
       "panVPNIkev2NegoChildFailTrap": panVPNIkev2NegoChildFailTrap,
       "panVPNIkev2NegoChildSuccTrap": panVPNIkev2NegoChildSuccTrap,
       "panVPNTunnelStatusUpTrap": panVPNTunnelStatusUpTrap,
       "panVPNTunnelStatusDownTrap": panVPNTunnelStatusDownTrap,
       "panVPNKeymgrDaemonStartTrap": panVPNKeymgrDaemonStartTrap,
       "panVPNKeymgrDaemonExitTrap": panVPNKeymgrDaemonExitTrap,
       "panVPNKeymgrDaemonInitTrap": panVPNKeymgrDaemonInitTrap,
       "panVPNKeymgrFlowFullSyncStartTrap": panVPNKeymgrFlowFullSyncStartTrap,
       "panVPNKeymgrFlowFullSyncAbortTrap": panVPNKeymgrFlowFullSyncAbortTrap,
       "panVPNKeymgrFlowFullSyncDoneTrap": panVPNKeymgrFlowFullSyncDoneTrap,
       "panVPNKeymgrIkeFullSyncStartTrap": panVPNKeymgrIkeFullSyncStartTrap,
       "panVPNKeymgrIkeFullSyncAbortTrap": panVPNKeymgrIkeFullSyncAbortTrap,
       "panVPNKeymgrIkeFullSyncDoneTrap": panVPNKeymgrIkeFullSyncDoneTrap,
       "panVPNKeymgrHaFullSyncStartTrap": panVPNKeymgrHaFullSyncStartTrap,
       "panVPNKeymgrHaFullSyncAbortTrap": panVPNKeymgrHaFullSyncAbortTrap,
       "panVPNKeymgrHaFullSyncDoneTrap": panVPNKeymgrHaFullSyncDoneTrap,
       "panVPNIkeGenericEventTrap": panVPNIkeGenericEventTrap,
       "panVPNKeymgrGenericEventTrap": panVPNKeymgrGenericEventTrap,
       "panVPNIkeNegoP1FailCertTrap": panVPNIkeNegoP1FailCertTrap,
       "panVPNIkeNegoP1CertIdMismatchTrap": panVPNIkeNegoP1CertIdMismatchTrap,
       "panVPNIkeNegoP1CertSuccTrap": panVPNIkeNegoP1CertSuccTrap,
       "panVPNIkev2NegoIkeDpdDnTrap": panVPNIkev2NegoIkeDpdDnTrap,
       "panVPNIkev2NegoPskIdtypeTrap": panVPNIkev2NegoPskIdtypeTrap,
       "panVPNIkev2NegoFailPskTrap": panVPNIkev2NegoFailPskTrap,
       "panVPNIkev2NegoFailCommonTrap": panVPNIkev2NegoFailCommonTrap,
       "panVPNIkev2NegoFailCertTrap": panVPNIkev2NegoFailCertTrap,
       "panVPNIkev2NegoCertIdMismatchTrap": panVPNIkev2NegoCertIdMismatchTrap,
       "panVPNIkev2NegoCertSuccTrap": panVPNIkev2NegoCertSuccTrap,
       "panVPNIkev2NegoUseV1Trap": panVPNIkev2NegoUseV1Trap,
       "panVPNIkev2NegoStaleP1Trap": panVPNIkev2NegoStaleP1Trap,
       "panVPNIkev2NegoStaleP2Trap": panVPNIkev2NegoStaleP2Trap,
       "panVPNIkev2NegoChildDupRekeyTrap": panVPNIkev2NegoChildDupRekeyTrap,
       "panVPNIkev2NegoChildSimulContTrap": panVPNIkev2NegoChildSimulContTrap,
       "panVPNIkev2NegoChildSimulFailTrap": panVPNIkev2NegoChildSimulFailTrap,
       "panVPNIkev2NegoChildSimulDelayTrap": panVPNIkev2NegoChildSimulDelayTrap,
       "panVPNIkev2NegoChildNoP1Trap": panVPNIkev2NegoChildNoP1Trap,
       "panVPNIkev2NegoChildP1NotReadyTrap": panVPNIkev2NegoChildP1NotReadyTrap,
       "panVPNIkev2NegoChildTsBadTrap": panVPNIkev2NegoChildTsBadTrap,
       "panVPNIkev2NegoChildProposalBadTrap": panVPNIkev2NegoChildProposalBadTrap,
       "panVPNIkev2RecvNotifyTrap": panVPNIkev2RecvNotifyTrap,
       "panVPNIkev2RecvP1DeleteTrap": panVPNIkev2RecvP1DeleteTrap,
       "panVPNIkev2RecvP2DeleteTrap": panVPNIkev2RecvP2DeleteTrap,
       "panVPNIkev2SendNotifyTrap": panVPNIkev2SendNotifyTrap,
       "panVPNIkev2SendP1DeleteTrap": panVPNIkev2SendP1DeleteTrap,
       "panVPNIkev2SendP2DeleteTrap": panVPNIkev2SendP2DeleteTrap,
       "panVPNSdwanTunnelStatusUpTrap": panVPNSdwanTunnelStatusUpTrap,
       "panVPNSdwanTunnelStatusDownTrap": panVPNSdwanTunnelStatusDownTrap,
       "panSATDSatdConfigP1SuccessTrap": panSATDSatdConfigP1SuccessTrap,
       "panSATDSatdConfigP1FailedTrap": panSATDSatdConfigP1FailedTrap,
       "panSATDSatdConfigP1AbortTrap": panSATDSatdConfigP1AbortTrap,
       "panSATDSatdConfigP2SuccessTrap": panSATDSatdConfigP2SuccessTrap,
       "panSATDSatdConfigP2FailedTrap": panSATDSatdConfigP2FailedTrap,
       "panSATDSatdDaemonStartTrap": panSATDSatdDaemonStartTrap,
       "panSATDSatdDaemonExitTrap": panSATDSatdDaemonExitTrap,
       "panSATDSatdDaemonInitTrap": panSATDSatdDaemonInitTrap,
       "panSATDSatdTunUpTrap": panSATDSatdTunUpTrap,
       "panSATDSatdTunDownTrap": panSATDSatdTunDownTrap,
       "panSATDSatdDupSubnetsTrap": panSATDSatdDupSubnetsTrap,
       "panSATDSatdDeniedRoutesTrap": panSATDSatdDeniedRoutesTrap,
       "panSATDSatdPortalGatewayDuplicateTrap": panSATDSatdPortalGatewayDuplicateTrap,
       "panSATDSatdFlowFullSyncStartTrap": panSATDSatdFlowFullSyncStartTrap,
       "panSATDSatdFlowFullSyncAbortTrap": panSATDSatdFlowFullSyncAbortTrap,
       "panSATDSatdFlowFullSyncDoneTrap": panSATDSatdFlowFullSyncDoneTrap,
       "panSATDSatdHaFullSyncStartTrap": panSATDSatdHaFullSyncStartTrap,
       "panSATDSatdHaFullSyncAbortTrap": panSATDSatdHaFullSyncAbortTrap,
       "panSATDSatdHaFullSyncDoneTrap": panSATDSatdHaFullSyncDoneTrap,
       "panSATDSatdIpAssignFailTrap": panSATDSatdIpAssignFailTrap,
       "panSATDSatdIpResetFailTrap": panSATDSatdIpResetFailTrap,
       "panSATDSatdTunMonDownTrap": panSATDSatdTunMonDownTrap,
       "panSATDSatdTunMonUpTrap": panSATDSatdTunMonUpTrap,
       "panSATDSatdTunSoftlifetimeExpiredTrap": panSATDSatdTunSoftlifetimeExpiredTrap,
       "panSATDSatdTunHardlifetimeExpiredTrap": panSATDSatdTunHardlifetimeExpiredTrap,
       "panSATDSatdAccRouteUpdFailTrap": panSATDSatdAccRouteUpdFailTrap,
       "panSATDSatdNhUpdFailTrap": panSATDSatdNhUpdFailTrap,
       "panSATDSatdTunDpInstallErrTrap": panSATDSatdTunDpInstallErrTrap,
       "panSATDSatdGatewayConnectStartedTrap": panSATDSatdGatewayConnectStartedTrap,
       "panSATDSatdPortalConnectStartedTrap": panSATDSatdPortalConnectStartedTrap,
       "panSATDSatdGatewayConnectFailedTrap": panSATDSatdGatewayConnectFailedTrap,
       "panSATDSatdPortalConnectFailedTrap": panSATDSatdPortalConnectFailedTrap,
       "panSATDSatdGenericEventTrap": panSATDSatdGenericEventTrap,
       "panSSLMGRSslmgrConfigP1SuccessTrap": panSSLMGRSslmgrConfigP1SuccessTrap,
       "panSSLMGRSslmgrConfigP1FailedTrap": panSSLMGRSslmgrConfigP1FailedTrap,
       "panSSLMGRSslmgrConfigP1AbortTrap": panSSLMGRSslmgrConfigP1AbortTrap,
       "panSSLMGRSslmgrConfigP2SuccessTrap": panSSLMGRSslmgrConfigP2SuccessTrap,
       "panSSLMGRSslmgrConfigP2FailedTrap": panSSLMGRSslmgrConfigP2FailedTrap,
       "panSSLMGRSslmgrDaemonStartTrap": panSSLMGRSslmgrDaemonStartTrap,
       "panSSLMGRSslmgrDaemonExitTrap": panSSLMGRSslmgrDaemonExitTrap,
       "panSSLMGRSslmgrCertGenSuccessTrap": panSSLMGRSslmgrCertGenSuccessTrap,
       "panSSLMGRSslmgrCertGenFailedTrap": panSSLMGRSslmgrCertGenFailedTrap,
       "panSSLMGRSslmgrCertStatusDeletedTrap": panSSLMGRSslmgrCertStatusDeletedTrap,
       "panSSLMGRSslmgrCertStatusRevokedTrap": panSSLMGRSslmgrCertStatusRevokedTrap,
       "panSSLMGRSslmgrSatelliteInfoInsertedTrap": panSSLMGRSslmgrSatelliteInfoInsertedTrap,
       "panSSLMGRSslmgrSatelliteInfoUpdatedTrap": panSSLMGRSslmgrSatelliteInfoUpdatedTrap,
       "panSSLMGRSslmgrSatelliteInfoDeletedTrap": panSSLMGRSslmgrSatelliteInfoDeletedTrap,
       "panSSLMGRSslmgrCertOcspVerifyFailedTrap": panSSLMGRSslmgrCertOcspVerifyFailedTrap,
       "panSSLMGRSslmgrCertCrlVerifyFailedTrap": panSSLMGRSslmgrCertCrlVerifyFailedTrap,
       "panSSLMGRSslmgrHaFullSyncTrap": panSSLMGRSslmgrHaFullSyncTrap,
       "panSSLMGRSslmgrHaNotFullSyncTrap": panSSLMGRSslmgrHaNotFullSyncTrap,
       "panSSLMGRSslmgrGenericEventTrap": panSSLMGRSslmgrGenericEventTrap,
       "panSSLMGRSslmgrScepCertSuccessTrap": panSSLMGRSslmgrScepCertSuccessTrap,
       "panSSLMGRSslmgrScepCertFailedTrap": panSSLMGRSslmgrScepCertFailedTrap,
       "panSSLMGRSslmgrScepCaCertSuccessTrap": panSSLMGRSslmgrScepCaCertSuccessTrap,
       "panSSLMGRSslmgrScepCaCertFailedTrap": panSSLMGRSslmgrScepCaCertFailedTrap,
       "panSSLMGRCaSessionEstablishmentSuccessTrap": panSSLMGRCaSessionEstablishmentSuccessTrap,
       "panSSLMGRCaSessionEstablishmentFailedTrap": panSSLMGRCaSessionEstablishmentFailedTrap,
       "panURLNoUrlDatabaseTrap": panURLNoUrlDatabaseTrap,
       "panURLInvalidLicenseTrap": panURLInvalidLicenseTrap,
       "panURLFailedToLockUpdateTrap": panURLFailedToLockUpdateTrap,
       "panURLConnectionSuccessTrap": panURLConnectionSuccessTrap,
       "panURLConnectionFailureTrap": panURLConnectionFailureTrap,
       "panURLServerIsDownTrap": panURLServerIsDownTrap,
       "panURLProxyConnectionFailureTrap": panURLProxyConnectionFailureTrap,
       "panURLReceiveDataFailureTrap": panURLReceiveDataFailureTrap,
       "panURLDynamicUrlConnectionDownTrap": panURLDynamicUrlConnectionDownTrap,
       "panURLDownloadingUrlDatabaseTrap": panURLDownloadingUrlDatabaseTrap,
       "panURLDownloadUrlDatabaseSuccessTrap": panURLDownloadUrlDatabaseSuccessTrap,
       "panURLUpgradeUrlDatabaseSuccessTrap": panURLUpgradeUrlDatabaseSuccessTrap,
       "panURLRevertUrlDatabaseSuccessTrap": panURLRevertUrlDatabaseSuccessTrap,
       "panURLUrlDatabaseIsLatestTrap": panURLUrlDatabaseIsLatestTrap,
       "panURLUrlDownloadFailureTrap": panURLUrlDownloadFailureTrap,
       "panURLUrlCloudConnectionFailureTrap": panURLUrlCloudConnectionFailureTrap,
       "panURLUrlCloudConnectionSuccessTrap": panURLUrlCloudConnectionSuccessTrap,
       "panURLUrlBackupSeedSuccessTrap": panURLUrlBackupSeedSuccessTrap,
       "panURLUrlBackupSeedFailureTrap": panURLUrlBackupSeedFailureTrap,
       "panURLCloudElectionTrap": panURLCloudElectionTrap,
       "panURLCloudProcessStartsTrap": panURLCloudProcessStartsTrap,
       "panURLCloudProcessStoppedTrap": panURLCloudProcessStoppedTrap,
       "panURLUpdateVersionFailureTrap": panURLUpdateVersionFailureTrap,
       "panURLErrorMsgFromCloudTrap": panURLErrorMsgFromCloudTrap,
       "panURLTestASiteTrap": panURLTestASiteTrap,
       "panURLUrlEngineStoppedTrap": panURLUrlEngineStoppedTrap,
       "panURLUrlEngineStartsTrap": panURLUrlEngineStartsTrap,
       "panURLStartupFailureTrap": panURLStartupFailureTrap,
       "panURLHaSyncFailureTrap": panURLHaSyncFailureTrap,
       "panURLHaSyncSuccessTrap": panURLHaSyncSuccessTrap,
       "panURLSaveMpCacheToDiscFailureTrap": panURLSaveMpCacheToDiscFailureTrap,
       "panURLSaveMpCacheToDiscSuccessTrap": panURLSaveMpCacheToDiscSuccessTrap,
       "panURLRfsProcessStartsTrap": panURLRfsProcessStartsTrap,
       "panURLRfsProcessStoppedTrap": panURLRfsProcessStoppedTrap,
       "panURLRfsProcessFailureTrap": panURLRfsProcessFailureTrap,
       "panURLRequestToCloudFailureTrap": panURLRequestToCloudFailureTrap,
       "panURLStartsFromEmptySeedTrap": panURLStartsFromEmptySeedTrap,
       "panURLLoadSuccessTrap": panURLLoadSuccessTrap,
       "panURLFailedToLockDownloadTrap": panURLFailedToLockDownloadTrap,
       "panURLEngineStartupFailureTrap": panURLEngineStartupFailureTrap,
       "panURLSeedOutOfSyncTrap": panURLSeedOutOfSyncTrap,
       "panURLStartsFromBackupSeedTrap": panURLStartsFromBackupSeedTrap,
       "panURLStartsFromDownloadSeedTrap": panURLStartsFromDownloadSeedTrap,
       "panURLBackupSeedErrorTrap": panURLBackupSeedErrorTrap,
       "panURLDownloadSeedErrorTrap": panURLDownloadSeedErrorTrap,
       "panUSERIDConnectAgentTrap": panUSERIDConnectAgentTrap,
       "panUSERIDDisconnectAgentTrap": panUSERIDDisconnectAgentTrap,
       "panUSERIDAgentEventTrap": panUSERIDAgentEventTrap,
       "panUSERIDConnectAgentFailureTrap": panUSERIDConnectAgentFailureTrap,
       "panUSERIDAgentVersionMismatchTrap": panUSERIDAgentVersionMismatchTrap,
       "panUSERIDAgentStatusFailureTrap": panUSERIDAgentStatusFailureTrap,
       "panUSERIDAgentReadLogErrorTrap": panUSERIDAgentReadLogErrorTrap,
       "panUSERIDAgentGetDomainErrorTrap": panUSERIDAgentGetDomainErrorTrap,
       "panUSERIDAgentGetUsersErrorTrap": panUSERIDAgentGetUsersErrorTrap,
       "panUSERIDAgentGetGroupsErrorTrap": panUSERIDAgentGetGroupsErrorTrap,
       "panUSERIDAgentGetConfigErrorTrap": panUSERIDAgentGetConfigErrorTrap,
       "panUSERIDAgentNoDomainTrap": panUSERIDAgentNoDomainTrap,
       "panUSERIDAgentNoAllowlistTrap": panUSERIDAgentNoAllowlistTrap,
       "panUSERIDConnectLdapSeverTrap": panUSERIDConnectLdapSeverTrap,
       "panUSERIDConnectLdapSeverFailureTrap": panUSERIDConnectLdapSeverFailureTrap,
       "panUSERIDGetLdapDataFailureTrap": panUSERIDGetLdapDataFailureTrap,
       "panUSERIDHAQueueFullTrap": panUSERIDHAQueueFullTrap,
       "panUSERIDConnectClientTrap": panUSERIDConnectClientTrap,
       "panUSERIDDisconnectClientTrap": panUSERIDDisconnectClientTrap,
       "panUSERIDConnectServerMonitorTrap": panUSERIDConnectServerMonitorTrap,
       "panUSERIDConnectServerMonitorFailureTrap": panUSERIDConnectServerMonitorFailureTrap,
       "panUSERIDConnectVmInfoSourceTrap": panUSERIDConnectVmInfoSourceTrap,
       "panUSERIDDisconnectVmInfoSourceTrap": panUSERIDDisconnectVmInfoSourceTrap,
       "panUSERIDConnectVmInfoSourceFailureTrap": panUSERIDConnectVmInfoSourceFailureTrap,
       "panUSERIDRegisteredIpUpdateFailureTrap": panUSERIDRegisteredIpUpdateFailureTrap,
       "panUSERIDConnectSyslogTrap": panUSERIDConnectSyslogTrap,
       "panUSERIDDisconnectSyslogTrap": panUSERIDDisconnectSyslogTrap,
       "panUSERIDUserGroupCountTrap": panUSERIDUserGroupCountTrap,
       "panUSERIDUserCountTrap": panUSERIDUserCountTrap,
       "panUSERIDGlobalprotectgatewayInvalidLicenseTrap": panUSERIDGlobalprotectgatewayInvalidLicenseTrap,
       "panNATFallbackReportTrap": panNATFallbackReportTrap,
       "panSYSLOGNGSyslogConnStatusTrap": panSYSLOGNGSyslogConnStatusTrap,
       "panLACPLostConnectivityTrap": panLACPLostConnectivityTrap,
       "panLACPUnresponsiveTrap": panLACPUnresponsiveTrap,
       "panLACPNegoFailTrap": panLACPNegoFailTrap,
       "panLACPSpeedDuplexTrap": panLACPSpeedDuplexTrap,
       "panLACPLinkDownTrap": panLACPLinkDownTrap,
       "panLACPLacpDownTrap": panLACPLacpDownTrap,
       "panLACPLacpUpTrap": panLACPLacpUpTrap,
       "panFIPSFipsSelftestUnknownTrap": panFIPSFipsSelftestUnknownTrap,
       "panFIPSFipsSelftestTimeoutTrap": panFIPSFipsSelftestTimeoutTrap,
       "panFIPSFipsSelftestIntegTrap": panFIPSFipsSelftestIntegTrap,
       "panFIPSFipsSelftestCoreTrap": panFIPSFipsSelftestCoreTrap,
       "panFIPSFipsSelftestAesTrap": panFIPSFipsSelftestAesTrap,
       "panFIPSFipsSelftestDesTrap": panFIPSFipsSelftestDesTrap,
       "panFIPSFipsSelftestDsaTrap": panFIPSFipsSelftestDsaTrap,
       "panFIPSFipsSelftestRsaTrap": panFIPSFipsSelftestRsaTrap,
       "panFIPSFipsSelftestHmacTrap": panFIPSFipsSelftestHmacTrap,
       "panFIPSFipsSelftestShaTrap": panFIPSFipsSelftestShaTrap,
       "panFIPSFipsSelftestDrngTrap": panFIPSFipsSelftestDrngTrap,
       "panFIPSFipsSelftestNdrngTrap": panFIPSFipsSelftestNdrngTrap,
       "panFIPSFipsSelftestDhParameterTrap": panFIPSFipsSelftestDhParameterTrap,
       "panFIPSFipsSelftestDhTrap": panFIPSFipsSelftestDhTrap,
       "panFIPSFipsFirmwareIntegrityTrap": panFIPSFipsFirmwareIntegrityTrap,
       "panFIPSFipsContinuousRngTrap": panFIPSFipsContinuousRngTrap,
       "panFIPSFipsRsaPairwiseConsistencyTrap": panFIPSFipsRsaPairwiseConsistencyTrap,
       "panFIPSFipsSelftestSoftwareLoadTrap": panFIPSFipsSelftestSoftwareLoadTrap,
       "panFIPSFipsSelftestTrap": panFIPSFipsSelftestTrap,
       "panFIPSFipsSelftestHsmTrap": panFIPSFipsSelftestHsmTrap,
       "panFIPSFipsZeroizationTrap": panFIPSFipsZeroizationTrap,
       "panFIPSFipsKeyTrap": panFIPSFipsKeyTrap,
       "panFIPSFipsCipherTrap": panFIPSFipsCipherTrap,
       "panFIPSFipsReplayTrap": panFIPSFipsReplayTrap,
       "panFIPSFipsSslHandshakeTrap": panFIPSFipsSslHandshakeTrap,
       "panFIPSFipsContinuousNdrngTrap": panFIPSFipsContinuousNdrngTrap,
       "panFIPSFipsSelftestCmacTrap": panFIPSFipsSelftestCmacTrap,
       "panFIPSFipsSelftestDrbgTrap": panFIPSFipsSelftestDrbgTrap,
       "panFIPSFipsSelftestEcdsaTrap": panFIPSFipsSelftestEcdsaTrap,
       "panFIPSFipsSelftestEcdhTrap": panFIPSFipsSelftestEcdhTrap,
       "panMDMExceedLicenseTrap": panMDMExceedLicenseTrap,
       "panMDMConnectToApnsTrap": panMDMConnectToApnsTrap,
       "panMDMConnectToApnsFailureTrap": panMDMConnectToApnsFailureTrap,
       "panMDMConnectToGcmTrap": panMDMConnectToGcmTrap,
       "panMDMConnectToGcmFailureTrap": panMDMConnectToGcmFailureTrap,
       "panMDMGatewayConnectedTrap": panMDMGatewayConnectedTrap,
       "panMDMGatewayDisconnectedTrap": panMDMGatewayDisconnectedTrap,
       "panMDMInstallAppContentTrap": panMDMInstallAppContentTrap,
       "panMDMInstallAppContentFailureTrap": panMDMInstallAppContentFailureTrap,
       "panMDMGetScepOtpFailureTrap": panMDMGetScepOtpFailureTrap,
       "panMDMSendMsgToCloudFailureTrap": panMDMSendMsgToCloudFailureTrap,
       "panMDMConnectToItunesFailureTrap": panMDMConnectToItunesFailureTrap,
       "panMDMConnectToAppleVppFailureTrap": panMDMConnectToAppleVppFailureTrap,
       "panRAIDDiskNotDetectedTrap": panRAIDDiskNotDetectedTrap,
       "panRAIDPairDetectedTrap": panRAIDPairDetectedTrap,
       "panRAIDRebuildingTrap": panRAIDRebuildingTrap,
       "panRAIDRebuild20Trap": panRAIDRebuild20Trap,
       "panRAIDRebuild40Trap": panRAIDRebuild40Trap,
       "panRAIDRebuild60Trap": panRAIDRebuild60Trap,
       "panRAIDRebuild80Trap": panRAIDRebuild80Trap,
       "panRAIDRebuildDoneTrap": panRAIDRebuildDoneTrap,
       "panRAIDDiskActiveTrap": panRAIDDiskActiveTrap,
       "panRAIDDiskFaultyTrap": panRAIDDiskFaultyTrap,
       "panRAIDDiskFailedTrap": panRAIDDiskFailedTrap,
       "panRAIDSpareMissingTrap": panRAIDSpareMissingTrap,
       "panRAIDSpareMovedTrap": panRAIDSpareMovedTrap,
       "panRAIDPairDegradedTrap": panRAIDPairDegradedTrap,
       "panRAIDPairDisappearedTrap": panRAIDPairDisappearedTrap,
       "panRAIDDiskRemovedTrap": panRAIDDiskRemovedTrap,
       "panRAIDFsckStartTrap": panRAIDFsckStartTrap,
       "panRAIDFsckEndTrap": panRAIDFsckEndTrap,
       "panRAIDFsckFailedTrap": panRAIDFsckFailedTrap,
       "panRAIDMountFailedTrap": panRAIDMountFailedTrap,
       "panRAIDRebuildFailedTrap": panRAIDRebuildFailedTrap,
       "panVMDvfInitSucceedTrap": panVMDvfInitSucceedTrap,
       "panVMDvfInitFailTrap": panVMDvfInitFailTrap,
       "panSSHSshSessionEstablishedTrap": panSSHSshSessionEstablishedTrap,
       "panSSHSshSessionTerminatedTrap": panSSHSshSessionTerminatedTrap,
       "panSSHSshSessionEstablishmentFailedTrap": panSSHSshSessionEstablishmentFailedTrap,
       "panSSHSshSessionDisconnectedTrap": panSSHSshSessionDisconnectedTrap,
       "panSSHSshConnectionTrap": panSSHSshConnectionTrap,
       "panTLSTlsSessionEstablishedTrap": panTLSTlsSessionEstablishedTrap,
       "panTLSTlsSessionTerminatedTrap": panTLSTlsSessionTerminatedTrap,
       "panTLSTlsSessionEstablishmentFailedTrap": panTLSTlsSessionEstablishmentFailedTrap,
       "panTLSTlsSessionDisconnectedTrap": panTLSTlsSessionDisconnectedTrap,
       "panTLSTlsEdlAuthFailureTrap": panTLSTlsEdlAuthFailureTrap,
       "panTLSTlsX509ServerIdentFailedTrap": panTLSTlsX509ServerIdentFailedTrap,
       "panTLSTlsX509ValidationFailedTrap": panTLSTlsX509ValidationFailedTrap,
       "panTLSTlsX509EkuServerAuthFailedTrap": panTLSTlsX509EkuServerAuthFailedTrap,
       "panTLSTlsX509ClientIdentFailedTrap": panTLSTlsX509ClientIdentFailedTrap,
       "panTLSTlsX509EkuClientAuthFailedTrap": panTLSTlsX509EkuClientAuthFailedTrap,
       "panTLSTlsX509EkuClientAuthSuccessTrap": panTLSTlsX509EkuClientAuthSuccessTrap,
       "panTLSPanoramaAuthFailureTrap": panTLSPanoramaAuthFailureTrap,
       "panTLSPanoramaAuthSuccessTrap": panTLSPanoramaAuthSuccessTrap,
       "panTLSPanosAuthFailureTrap": panTLSPanosAuthFailureTrap,
       "panTLSPanosAuthSuccessTrap": panTLSPanosAuthSuccessTrap,
       "panTLSTlsX509EkuCodeSigningExtCheckFailedTrap": panTLSTlsX509EkuCodeSigningExtCheckFailedTrap,
       "panTLSTlsX509OcspCrlCheckFailedTrap": panTLSTlsX509OcspCrlCheckFailedTrap,
       "panTLSTlsX509UntrustedCertIssuerFoundTrap": panTLSTlsX509UntrustedCertIssuerFoundTrap,
       "panTLSMfaAuthFailureTrap": panTLSMfaAuthFailureTrap,
       "panTLSCertificateRenewalTrap": panTLSCertificateRenewalTrap,
       "panTLSCertificateExpiredTrap": panTLSCertificateExpiredTrap,
       "panLLDPRxErrorTrap": panLLDPRxErrorTrap,
       "panLLDPMibChangedTrap": panLLDPMibChangedTrap,
       "panLLDPTooManyNeighborsTrap": panLLDPTooManyNeighborsTrap,
       "panLLDPTooManyNeighborsTimerClearedTrap": panLLDPTooManyNeighborsTimerClearedTrap,
       "panLLDPOtherTrap": panLLDPOtherTrap,
       "panLLDPTxErrorTrap": panLLDPTxErrorTrap,
       "panFBWildfireWrongCloudTypeTrap": panFBWildfireWrongCloudTypeTrap,
       "panFBWildfireDisabledByCloudTrap": panFBWildfireDisabledByCloudTrap,
       "panFBWildfireNoPolicyTrap": panFBWildfireNoPolicyTrap,
       "panFBWildfireNoLicenseTrap": panFBWildfireNoLicenseTrap,
       "panFBWildfireInvalidCloudInfoTrap": panFBWildfireInvalidCloudInfoTrap,
       "panBFDExpiredTimeTrap": panBFDExpiredTimeTrap,
       "panBFDNeighborDownTrap": panBFDNeighborDownTrap,
       "panBFDForwardPlaneResetTrap": panBFDForwardPlaneResetTrap,
       "panBFDAdminDownTrap": panBFDAdminDownTrap,
       "panBFDSessionStateChangeTrap": panBFDSessionStateChangeTrap,
       "panAUTHGeneralTrap": panAUTHGeneralTrap,
       "panAUTHAuthServerDownTrap": panAUTHAuthServerDownTrap,
       "panAUTHCreateAdminAcctErrorTrap": panAUTHCreateAdminAcctErrorTrap,
       "panAUTHAuthFailTrap": panAUTHAuthFailTrap,
       "panAUTHAuthSuccessTrap": panAUTHAuthSuccessTrap,
       "panAUTHSamlClientRedirectTrap": panAUTHSamlClientRedirectTrap,
       "panAUTHSamlIdpActivityTrap": panAUTHSamlIdpActivityTrap,
       "panAUTHSamlCertificateWarningTrap": panAUTHSamlCertificateWarningTrap,
       "panAUTHSamlCertificateErrorTrap": panAUTHSamlCertificateErrorTrap,
       "panAUTHSamlMessageParseErrorTrap": panAUTHSamlMessageParseErrorTrap,
       "panAUTHSamlOutOfBandMessageTrap": panAUTHSamlOutOfBandMessageTrap,
       "panAUTHSamlSignatureValidatedTrap": panAUTHSamlSignatureValidatedTrap,
       "panAUTHEdlCliAuthFailureTrap": panAUTHEdlCliAuthFailureTrap,
       "panAUTHLogoutSuccessTrap": panAUTHLogoutSuccessTrap,
       "panAUTHLogoutFailedTrap": panAUTHLogoutFailedTrap,
       "panAUTHIdpInitiatedLogOutSuccessTrap": panAUTHIdpInitiatedLogOutSuccessTrap,
       "panAUTHSpInitiatedLogOutSuccessTrap": panAUTHSpInitiatedLogOutSuccessTrap,
       "panAUTHUserPasswordChangeSuccessTrap": panAUTHUserPasswordChangeSuccessTrap,
       "panAUTHUserPasswordChangeFailedTrap": panAUTHUserPasswordChangeFailedTrap,
       "panCLUSTERDClusterDaemonInitTrap": panCLUSTERDClusterDaemonInitTrap,
       "panCLUSTERDClusterDaemonStartTrap": panCLUSTERDClusterDaemonStartTrap,
       "panCLUSTERDClusterDaemonExitTrap": panCLUSTERDClusterDaemonExitTrap,
       "panCLUSTERDClusterDaemonCfgTrap": panCLUSTERDClusterDaemonCfgTrap,
       "panCLUSTERDClusterDaemonCfgGiveupTrap": panCLUSTERDClusterDaemonCfgGiveupTrap,
       "panCLUSTERDClusterHaSyncPeerBackupTrap": panCLUSTERDClusterHaSyncPeerBackupTrap,
       "panCLUSTERDClusterHaSyncSelfMasterTrap": panCLUSTERDClusterHaSyncSelfMasterTrap,
       "panCLUSTERDClusterConfigP1SuccessTrap": panCLUSTERDClusterConfigP1SuccessTrap,
       "panCLUSTERDClusterConfigP1FailedTrap": panCLUSTERDClusterConfigP1FailedTrap,
       "panCLUSTERDClusterConfigP1AbortTrap": panCLUSTERDClusterConfigP1AbortTrap,
       "panCLUSTERDClusterConfigP2SuccessTrap": panCLUSTERDClusterConfigP2SuccessTrap,
       "panCLUSTERDClusterConfigP2FailedTrap": panCLUSTERDClusterConfigP2FailedTrap,
       "panCLUSTERDClusterEngineControllerTrap": panCLUSTERDClusterEngineControllerTrap,
       "panCLUSTERDClusterEngineServerTrap": panCLUSTERDClusterEngineServerTrap,
       "panCLUSTERDClusterEngineWorkerTrap": panCLUSTERDClusterEngineWorkerTrap,
       "panCLUSTERDClusterEngineReloadTrap": panCLUSTERDClusterEngineReloadTrap,
       "panCLUSTERDClusterEngineRestartTrap": panCLUSTERDClusterEngineRestartTrap,
       "panCLUSTERDClusterEngineShutdownTrap": panCLUSTERDClusterEngineShutdownTrap,
       "panCLUSTERDClusterSelfJoinTrap": panCLUSTERDClusterSelfJoinTrap,
       "panCLUSTERDClusterSelfDownTrap": panCLUSTERDClusterSelfDownTrap,
       "panCLUSTERDClusterSelfLeaveTrap": panCLUSTERDClusterSelfLeaveTrap,
       "panCLUSTERDClusterOtherJoinTrap": panCLUSTERDClusterOtherJoinTrap,
       "panCLUSTERDClusterOtherDownTrap": panCLUSTERDClusterOtherDownTrap,
       "panCLUSTERDClusterOtherLeaveTrap": panCLUSTERDClusterOtherLeaveTrap,
       "panIPV6NDIpv6DisabledTrap": panIPV6NDIpv6DisabledTrap,
       "panIPV6NDDuplicatedIPv6AddressFoundTrap": panIPV6NDDuplicatedIPv6AddressFoundTrap,
       "panIPV6NDInconsistentRaMessageReceivedTrap": panIPV6NDInconsistentRaMessageReceivedTrap,
       "panDYNAMICUPDATESPaloAltoNetworksMessageTrap": panDYNAMICUPDATESPaloAltoNetworksMessageTrap,
       "panUUIDPolicyRuleUuidModifiedTrap": panUUIDPolicyRuleUuidModifiedTrap,
       "panGRETunnelStatusUpTrap": panGRETunnelStatusUpTrap,
       "panGRETunnelStatusDownTrap": panGRETunnelStatusDownTrap,
       "panGRETunnelRecurRoutingTrap": panGRETunnelRecurRoutingTrap,
       "panPANOCHECKPanoramaCheckSkipTrap": panPANOCHECKPanoramaCheckSkipTrap,
       "panPANOCHECKPanoramaCheckAutoDisabledTrap": panPANOCHECKPanoramaCheckAutoDisabledTrap,
       "panPANOCHECKPanoramaCheckAutoRevertTrap": panPANOCHECKPanoramaCheckAutoRevertTrap,
       "panPANOCHECKPanoramaCheckTestTrap": panPANOCHECKPanoramaCheckTestTrap,
       "panSDWANSdwanVifStatusUpTrap": panSDWANSdwanVifStatusUpTrap,
       "panSDWANSdwanVifStatusDownTrap": panSDWANSdwanVifStatusDownTrap}
)
