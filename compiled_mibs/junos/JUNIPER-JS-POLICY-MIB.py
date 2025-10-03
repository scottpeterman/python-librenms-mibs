# SNMP MIB module (JUNIPER-JS-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-JS-POLICY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:32 2025
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

(jnxJsPolicies,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsPolicies")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

jnxJsSecPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxJsSecPolicyMIB.setRevisions(
        ("2006-12-14 00:00",
         "2013-07-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsPolicyNotifications_ObjectIdentity = ObjectIdentity
jnxJsPolicyNotifications = _JnxJsPolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 0)
)
_JnxJsPolicyObjects_ObjectIdentity = ObjectIdentity
jnxJsPolicyObjects = _JnxJsPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1)
)
_JnxJsPolicyNumber_Type = Integer32
_JnxJsPolicyNumber_Object = MibScalar
jnxJsPolicyNumber = _JnxJsPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 1),
    _JnxJsPolicyNumber_Type()
)
jnxJsPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyNumber.setStatus("current")
_JnxJsPolicyTable_Object = MibTable
jnxJsPolicyTable = _JnxJsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJsPolicyTable.setStatus("current")
_JnxJsPolicyEntry_Object = MibTableRow
jnxJsPolicyEntry = _JnxJsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1)
)
jnxJsPolicyEntry.setIndexNames(
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"),
)
if mibBuilder.loadTexts:
    jnxJsPolicyEntry.setStatus("current")


class _JnxJsPolicyFromZone_Type(DisplayString):
    """Custom type jnxJsPolicyFromZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyFromZone_Type.__name__ = "DisplayString"
_JnxJsPolicyFromZone_Object = MibTableColumn
jnxJsPolicyFromZone = _JnxJsPolicyFromZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 1),
    _JnxJsPolicyFromZone_Type()
)
jnxJsPolicyFromZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyFromZone.setStatus("current")


class _JnxJsPolicyToZone_Type(DisplayString):
    """Custom type jnxJsPolicyToZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyToZone_Type.__name__ = "DisplayString"
_JnxJsPolicyToZone_Object = MibTableColumn
jnxJsPolicyToZone = _JnxJsPolicyToZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 2),
    _JnxJsPolicyToZone_Type()
)
jnxJsPolicyToZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyToZone.setStatus("current")


class _JnxJsPolicyName_Type(DisplayString):
    """Custom type jnxJsPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyName_Type.__name__ = "DisplayString"
_JnxJsPolicyName_Object = MibTableColumn
jnxJsPolicyName = _JnxJsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 3),
    _JnxJsPolicyName_Type()
)
jnxJsPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsPolicyName.setStatus("current")
_JnxJsPolicySequenceNumber_Type = Integer32
_JnxJsPolicySequenceNumber_Object = MibTableColumn
jnxJsPolicySequenceNumber = _JnxJsPolicySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 4),
    _JnxJsPolicySequenceNumber_Type()
)
jnxJsPolicySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySequenceNumber.setStatus("current")


class _JnxJsPolicyAction_Type(Integer32):
    """Custom type jnxJsPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("reject", 3))
    )


_JnxJsPolicyAction_Type.__name__ = "Integer32"
_JnxJsPolicyAction_Object = MibTableColumn
jnxJsPolicyAction = _JnxJsPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 5),
    _JnxJsPolicyAction_Type()
)
jnxJsPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyAction.setStatus("current")


class _JnxJsPolicyScheduler_Type(DisplayString):
    """Custom type jnxJsPolicyScheduler based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxJsPolicyScheduler_Type.__name__ = "DisplayString"
_JnxJsPolicyScheduler_Object = MibTableColumn
jnxJsPolicyScheduler = _JnxJsPolicyScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 6),
    _JnxJsPolicyScheduler_Type()
)
jnxJsPolicyScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyScheduler.setStatus("current")


class _JnxJsPolicyState_Type(Integer32):
    """Custom type jnxJsPolicyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unavailable", 3))
    )


_JnxJsPolicyState_Type.__name__ = "Integer32"
_JnxJsPolicyState_Object = MibTableColumn
jnxJsPolicyState = _JnxJsPolicyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 7),
    _JnxJsPolicyState_Type()
)
jnxJsPolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyState.setStatus("current")


class _JnxJsPolicyStatsAvailability_Type(Integer32):
    """Custom type jnxJsPolicyStatsAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_JnxJsPolicyStatsAvailability_Type.__name__ = "Integer32"
_JnxJsPolicyStatsAvailability_Object = MibTableColumn
jnxJsPolicyStatsAvailability = _JnxJsPolicyStatsAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 8),
    _JnxJsPolicyStatsAvailability_Type()
)
jnxJsPolicyStatsAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsAvailability.setStatus("current")
_JnxJsPolicyPerSecBytesThreshold_Type = Integer32
_JnxJsPolicyPerSecBytesThreshold_Object = MibTableColumn
jnxJsPolicyPerSecBytesThreshold = _JnxJsPolicyPerSecBytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 9),
    _JnxJsPolicyPerSecBytesThreshold_Type()
)
jnxJsPolicyPerSecBytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyPerSecBytesThreshold.setStatus("current")
_JnxJsPolicyPerMinKbytesThreshold_Type = Integer32
_JnxJsPolicyPerMinKbytesThreshold_Object = MibTableColumn
jnxJsPolicyPerMinKbytesThreshold = _JnxJsPolicyPerMinKbytesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 10),
    _JnxJsPolicyPerMinKbytesThreshold_Type()
)
jnxJsPolicyPerMinKbytesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyPerMinKbytesThreshold.setStatus("current")
_JnxJsPolicyStatsTable_Object = MibTable
jnxJsPolicyStatsTable = _JnxJsPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJsPolicyStatsTable.setStatus("current")
_JnxJsPolicyStatsEntry_Object = MibTableRow
jnxJsPolicyStatsEntry = _JnxJsPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1)
)
jnxJsPolicyStatsEntry.setIndexNames(
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"),
    (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"),
)
if mibBuilder.loadTexts:
    jnxJsPolicyStatsEntry.setStatus("current")
_JnxJsPolicyStatsCreationTime_Type = TimeStamp
_JnxJsPolicyStatsCreationTime_Object = MibTableColumn
jnxJsPolicyStatsCreationTime = _JnxJsPolicyStatsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 1),
    _JnxJsPolicyStatsCreationTime_Type()
)
jnxJsPolicyStatsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsCreationTime.setStatus("current")
_JnxJsPolicyStatsInputBytes_Type = Counter64
_JnxJsPolicyStatsInputBytes_Object = MibTableColumn
jnxJsPolicyStatsInputBytes = _JnxJsPolicyStatsInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 2),
    _JnxJsPolicyStatsInputBytes_Type()
)
jnxJsPolicyStatsInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputBytes.setStatus("current")
_JnxJsPolicyStatsInputByteRate_Type = Gauge32
_JnxJsPolicyStatsInputByteRate_Object = MibTableColumn
jnxJsPolicyStatsInputByteRate = _JnxJsPolicyStatsInputByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 3),
    _JnxJsPolicyStatsInputByteRate_Type()
)
jnxJsPolicyStatsInputByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputByteRate.setStatus("current")
_JnxJsPolicyStatsOutputBytes_Type = Counter64
_JnxJsPolicyStatsOutputBytes_Object = MibTableColumn
jnxJsPolicyStatsOutputBytes = _JnxJsPolicyStatsOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 4),
    _JnxJsPolicyStatsOutputBytes_Type()
)
jnxJsPolicyStatsOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputBytes.setStatus("current")
_JnxJsPolicyStatsOutputByteRate_Type = Gauge32
_JnxJsPolicyStatsOutputByteRate_Object = MibTableColumn
jnxJsPolicyStatsOutputByteRate = _JnxJsPolicyStatsOutputByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 5),
    _JnxJsPolicyStatsOutputByteRate_Type()
)
jnxJsPolicyStatsOutputByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputByteRate.setStatus("current")
_JnxJsPolicyStatsInputPackets_Type = Counter32
_JnxJsPolicyStatsInputPackets_Object = MibTableColumn
jnxJsPolicyStatsInputPackets = _JnxJsPolicyStatsInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 6),
    _JnxJsPolicyStatsInputPackets_Type()
)
jnxJsPolicyStatsInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputPackets.setStatus("current")
_JnxJsPolicyStatsInputPacketRate_Type = Gauge32
_JnxJsPolicyStatsInputPacketRate_Object = MibTableColumn
jnxJsPolicyStatsInputPacketRate = _JnxJsPolicyStatsInputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 7),
    _JnxJsPolicyStatsInputPacketRate_Type()
)
jnxJsPolicyStatsInputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInputPacketRate.setStatus("current")
_JnxJsPolicyStatsOutputPackets_Type = Counter32
_JnxJsPolicyStatsOutputPackets_Object = MibTableColumn
jnxJsPolicyStatsOutputPackets = _JnxJsPolicyStatsOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 8),
    _JnxJsPolicyStatsOutputPackets_Type()
)
jnxJsPolicyStatsOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputPackets.setStatus("current")
_JnxJsPolicyStatsOutputPacketRate_Type = Gauge32
_JnxJsPolicyStatsOutputPacketRate_Object = MibTableColumn
jnxJsPolicyStatsOutputPacketRate = _JnxJsPolicyStatsOutputPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 9),
    _JnxJsPolicyStatsOutputPacketRate_Type()
)
jnxJsPolicyStatsOutputPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutputPacketRate.setStatus("current")
_JnxJsPolicyStatsNumSessions_Type = Counter32
_JnxJsPolicyStatsNumSessions_Object = MibTableColumn
jnxJsPolicyStatsNumSessions = _JnxJsPolicyStatsNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 10),
    _JnxJsPolicyStatsNumSessions_Type()
)
jnxJsPolicyStatsNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsNumSessions.setStatus("current")
_JnxJsPolicyStatsSessionRate_Type = Gauge32
_JnxJsPolicyStatsSessionRate_Object = MibTableColumn
jnxJsPolicyStatsSessionRate = _JnxJsPolicyStatsSessionRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 11),
    _JnxJsPolicyStatsSessionRate_Type()
)
jnxJsPolicyStatsSessionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsSessionRate.setStatus("current")
_JnxJsPolicyStatsSessionDeleted_Type = Counter32
_JnxJsPolicyStatsSessionDeleted_Object = MibTableColumn
jnxJsPolicyStatsSessionDeleted = _JnxJsPolicyStatsSessionDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 12),
    _JnxJsPolicyStatsSessionDeleted_Type()
)
jnxJsPolicyStatsSessionDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsSessionDeleted.setStatus("current")
_JnxJsPolicyStatsLookups_Type = Counter32
_JnxJsPolicyStatsLookups_Object = MibTableColumn
jnxJsPolicyStatsLookups = _JnxJsPolicyStatsLookups_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 13),
    _JnxJsPolicyStatsLookups_Type()
)
jnxJsPolicyStatsLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsLookups.setStatus("current")
_JnxJsPolicyStatsCountAlarm_Type = Counter32
_JnxJsPolicyStatsCountAlarm_Object = MibTableColumn
jnxJsPolicyStatsCountAlarm = _JnxJsPolicyStatsCountAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 14),
    _JnxJsPolicyStatsCountAlarm_Type()
)
jnxJsPolicyStatsCountAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsCountAlarm.setStatus("obsolete")
_JnxJsPolicyStatsInBytesInit_Type = Counter64
_JnxJsPolicyStatsInBytesInit_Object = MibTableColumn
jnxJsPolicyStatsInBytesInit = _JnxJsPolicyStatsInBytesInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 15),
    _JnxJsPolicyStatsInBytesInit_Type()
)
jnxJsPolicyStatsInBytesInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInBytesInit.setStatus("current")
_JnxJsPolicyStatsInBytesRep_Type = Counter64
_JnxJsPolicyStatsInBytesRep_Object = MibTableColumn
jnxJsPolicyStatsInBytesRep = _JnxJsPolicyStatsInBytesRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 16),
    _JnxJsPolicyStatsInBytesRep_Type()
)
jnxJsPolicyStatsInBytesRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInBytesRep.setStatus("current")
_JnxJsPolicyStatsInByteRtInit_Type = Gauge32
_JnxJsPolicyStatsInByteRtInit_Object = MibTableColumn
jnxJsPolicyStatsInByteRtInit = _JnxJsPolicyStatsInByteRtInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 17),
    _JnxJsPolicyStatsInByteRtInit_Type()
)
jnxJsPolicyStatsInByteRtInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInByteRtInit.setStatus("current")
_JnxJsPolicyStatsInByteRtRep_Type = Gauge32
_JnxJsPolicyStatsInByteRtRep_Object = MibTableColumn
jnxJsPolicyStatsInByteRtRep = _JnxJsPolicyStatsInByteRtRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 18),
    _JnxJsPolicyStatsInByteRtRep_Type()
)
jnxJsPolicyStatsInByteRtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInByteRtRep.setStatus("current")
_JnxJsPolicyStatsOutBytesInit_Type = Counter64
_JnxJsPolicyStatsOutBytesInit_Object = MibTableColumn
jnxJsPolicyStatsOutBytesInit = _JnxJsPolicyStatsOutBytesInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 19),
    _JnxJsPolicyStatsOutBytesInit_Type()
)
jnxJsPolicyStatsOutBytesInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutBytesInit.setStatus("current")
_JnxJsPolicyStatsOutBytesRep_Type = Counter64
_JnxJsPolicyStatsOutBytesRep_Object = MibTableColumn
jnxJsPolicyStatsOutBytesRep = _JnxJsPolicyStatsOutBytesRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 20),
    _JnxJsPolicyStatsOutBytesRep_Type()
)
jnxJsPolicyStatsOutBytesRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutBytesRep.setStatus("current")
_JnxJsPolicyStatsOutByteRtInit_Type = Gauge32
_JnxJsPolicyStatsOutByteRtInit_Object = MibTableColumn
jnxJsPolicyStatsOutByteRtInit = _JnxJsPolicyStatsOutByteRtInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 21),
    _JnxJsPolicyStatsOutByteRtInit_Type()
)
jnxJsPolicyStatsOutByteRtInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutByteRtInit.setStatus("current")
_JnxJsPolicyStatsOutByteRtRep_Type = Gauge32
_JnxJsPolicyStatsOutByteRtRep_Object = MibTableColumn
jnxJsPolicyStatsOutByteRtRep = _JnxJsPolicyStatsOutByteRtRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 22),
    _JnxJsPolicyStatsOutByteRtRep_Type()
)
jnxJsPolicyStatsOutByteRtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutByteRtRep.setStatus("current")
_JnxJsPolicyStatsInPacketsInit_Type = Counter32
_JnxJsPolicyStatsInPacketsInit_Object = MibTableColumn
jnxJsPolicyStatsInPacketsInit = _JnxJsPolicyStatsInPacketsInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 23),
    _JnxJsPolicyStatsInPacketsInit_Type()
)
jnxJsPolicyStatsInPacketsInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInPacketsInit.setStatus("current")
_JnxJsPolicyStatsInPacketsRep_Type = Counter32
_JnxJsPolicyStatsInPacketsRep_Object = MibTableColumn
jnxJsPolicyStatsInPacketsRep = _JnxJsPolicyStatsInPacketsRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 24),
    _JnxJsPolicyStatsInPacketsRep_Type()
)
jnxJsPolicyStatsInPacketsRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInPacketsRep.setStatus("current")
_JnxJsPolicyStatsInPacketRtInit_Type = Gauge32
_JnxJsPolicyStatsInPacketRtInit_Object = MibTableColumn
jnxJsPolicyStatsInPacketRtInit = _JnxJsPolicyStatsInPacketRtInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 25),
    _JnxJsPolicyStatsInPacketRtInit_Type()
)
jnxJsPolicyStatsInPacketRtInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInPacketRtInit.setStatus("current")
_JnxJsPolicyStatsInPacketRtRep_Type = Gauge32
_JnxJsPolicyStatsInPacketRtRep_Object = MibTableColumn
jnxJsPolicyStatsInPacketRtRep = _JnxJsPolicyStatsInPacketRtRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 26),
    _JnxJsPolicyStatsInPacketRtRep_Type()
)
jnxJsPolicyStatsInPacketRtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsInPacketRtRep.setStatus("current")
_JnxJsPolicyStatsOutPacketsInit_Type = Counter32
_JnxJsPolicyStatsOutPacketsInit_Object = MibTableColumn
jnxJsPolicyStatsOutPacketsInit = _JnxJsPolicyStatsOutPacketsInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 27),
    _JnxJsPolicyStatsOutPacketsInit_Type()
)
jnxJsPolicyStatsOutPacketsInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutPacketsInit.setStatus("current")
_JnxJsPolicyStatsOutPacketsRep_Type = Counter32
_JnxJsPolicyStatsOutPacketsRep_Object = MibTableColumn
jnxJsPolicyStatsOutPacketsRep = _JnxJsPolicyStatsOutPacketsRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 28),
    _JnxJsPolicyStatsOutPacketsRep_Type()
)
jnxJsPolicyStatsOutPacketsRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutPacketsRep.setStatus("current")
_JnxJsPolicyStatsOutPacketRtInit_Type = Gauge32
_JnxJsPolicyStatsOutPacketRtInit_Object = MibTableColumn
jnxJsPolicyStatsOutPacketRtInit = _JnxJsPolicyStatsOutPacketRtInit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 29),
    _JnxJsPolicyStatsOutPacketRtInit_Type()
)
jnxJsPolicyStatsOutPacketRtInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutPacketRtInit.setStatus("current")
_JnxJsPolicyStatsOutPacketRtRep_Type = Gauge32
_JnxJsPolicyStatsOutPacketRtRep_Object = MibTableColumn
jnxJsPolicyStatsOutPacketRtRep = _JnxJsPolicyStatsOutPacketRtRep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 30),
    _JnxJsPolicyStatsOutPacketRtRep_Type()
)
jnxJsPolicyStatsOutPacketRtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicyStatsOutPacketRtRep.setStatus("current")
_JnxJsPolicyTrapVars_ObjectIdentity = ObjectIdentity
jnxJsPolicyTrapVars = _JnxJsPolicyTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 2)
)
_JnxJsPolicySystemStats_ObjectIdentity = ObjectIdentity
jnxJsPolicySystemStats = _JnxJsPolicySystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3)
)
_JnxJsPolicySystemStatsIPv4_ObjectIdentity = ObjectIdentity
jnxJsPolicySystemStatsIPv4 = _JnxJsPolicySystemStatsIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1)
)
_JnxJsPolicySystemStatsTotalAllowIPv4Packets_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv4Packets_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4Packets = _JnxJsPolicySystemStatsTotalAllowIPv4Packets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 1),
    _JnxJsPolicySystemStatsTotalAllowIPv4Packets_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4Packets.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv4Bytes_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv4Bytes_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4Bytes = _JnxJsPolicySystemStatsTotalAllowIPv4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 2),
    _JnxJsPolicySystemStatsTotalAllowIPv4Bytes_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4Bytes.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv4PacketsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv4PacketsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4PacketsRate = _JnxJsPolicySystemStatsTotalAllowIPv4PacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 3),
    _JnxJsPolicySystemStatsTotalAllowIPv4PacketsRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4PacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4PacketsRate.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv4BytesRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv4BytesRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4BytesRate = _JnxJsPolicySystemStatsTotalAllowIPv4BytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 4),
    _JnxJsPolicySystemStatsTotalAllowIPv4BytesRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4BytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4BytesRate.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv4Packets_Type = Counter64
_JnxJsPolicySystemStatsTotalDropIPv4Packets_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv4Packets = _JnxJsPolicySystemStatsTotalDropIPv4Packets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 5),
    _JnxJsPolicySystemStatsTotalDropIPv4Packets_Type()
)
jnxJsPolicySystemStatsTotalDropIPv4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv4Packets.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv4Bytes_Type = Counter64
_JnxJsPolicySystemStatsTotalDropIPv4Bytes_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv4Bytes = _JnxJsPolicySystemStatsTotalDropIPv4Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 6),
    _JnxJsPolicySystemStatsTotalDropIPv4Bytes_Type()
)
jnxJsPolicySystemStatsTotalDropIPv4Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv4Bytes.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv4PacketsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalDropIPv4PacketsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv4PacketsRate = _JnxJsPolicySystemStatsTotalDropIPv4PacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 7),
    _JnxJsPolicySystemStatsTotalDropIPv4PacketsRate_Type()
)
jnxJsPolicySystemStatsTotalDropIPv4PacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv4PacketsRate.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv4BytesRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalDropIPv4BytesRate_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv4BytesRate = _JnxJsPolicySystemStatsTotalDropIPv4BytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 8),
    _JnxJsPolicySystemStatsTotalDropIPv4BytesRate_Type()
)
jnxJsPolicySystemStatsTotalDropIPv4BytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv4BytesRate.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv4Flows_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv4Flows_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4Flows = _JnxJsPolicySystemStatsTotalAllowIPv4Flows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 9),
    _JnxJsPolicySystemStatsTotalAllowIPv4Flows_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4Flows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4Flows.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv4FlowsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv4FlowsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv4FlowsRate = _JnxJsPolicySystemStatsTotalAllowIPv4FlowsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 1, 10),
    _JnxJsPolicySystemStatsTotalAllowIPv4FlowsRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv4FlowsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv4FlowsRate.setStatus("current")
_JnxJsPolicySystemStatsIPv6_ObjectIdentity = ObjectIdentity
jnxJsPolicySystemStatsIPv6 = _JnxJsPolicySystemStatsIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2)
)
_JnxJsPolicySystemStatsTotalAllowIPv6Packets_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv6Packets_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6Packets = _JnxJsPolicySystemStatsTotalAllowIPv6Packets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 1),
    _JnxJsPolicySystemStatsTotalAllowIPv6Packets_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6Packets.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv6Bytes_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv6Bytes_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6Bytes = _JnxJsPolicySystemStatsTotalAllowIPv6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 2),
    _JnxJsPolicySystemStatsTotalAllowIPv6Bytes_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6Bytes.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv6PacketsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv6PacketsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6PacketsRate = _JnxJsPolicySystemStatsTotalAllowIPv6PacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 3),
    _JnxJsPolicySystemStatsTotalAllowIPv6PacketsRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6PacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6PacketsRate.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv6BytesRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv6BytesRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6BytesRate = _JnxJsPolicySystemStatsTotalAllowIPv6BytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 4),
    _JnxJsPolicySystemStatsTotalAllowIPv6BytesRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6BytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6BytesRate.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv6Packets_Type = Counter64
_JnxJsPolicySystemStatsTotalDropIPv6Packets_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv6Packets = _JnxJsPolicySystemStatsTotalDropIPv6Packets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 5),
    _JnxJsPolicySystemStatsTotalDropIPv6Packets_Type()
)
jnxJsPolicySystemStatsTotalDropIPv6Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv6Packets.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv6Bytes_Type = Counter64
_JnxJsPolicySystemStatsTotalDropIPv6Bytes_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv6Bytes = _JnxJsPolicySystemStatsTotalDropIPv6Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 6),
    _JnxJsPolicySystemStatsTotalDropIPv6Bytes_Type()
)
jnxJsPolicySystemStatsTotalDropIPv6Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv6Bytes.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv6PacketsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalDropIPv6PacketsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv6PacketsRate = _JnxJsPolicySystemStatsTotalDropIPv6PacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 7),
    _JnxJsPolicySystemStatsTotalDropIPv6PacketsRate_Type()
)
jnxJsPolicySystemStatsTotalDropIPv6PacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv6PacketsRate.setStatus("current")
_JnxJsPolicySystemStatsTotalDropIPv6BytesRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalDropIPv6BytesRate_Object = MibScalar
jnxJsPolicySystemStatsTotalDropIPv6BytesRate = _JnxJsPolicySystemStatsTotalDropIPv6BytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 8),
    _JnxJsPolicySystemStatsTotalDropIPv6BytesRate_Type()
)
jnxJsPolicySystemStatsTotalDropIPv6BytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalDropIPv6BytesRate.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv6Flows_Type = Counter64
_JnxJsPolicySystemStatsTotalAllowIPv6Flows_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6Flows = _JnxJsPolicySystemStatsTotalAllowIPv6Flows_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 9),
    _JnxJsPolicySystemStatsTotalAllowIPv6Flows_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6Flows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6Flows.setStatus("current")
_JnxJsPolicySystemStatsTotalAllowIPv6FlowsRate_Type = Gauge32
_JnxJsPolicySystemStatsTotalAllowIPv6FlowsRate_Object = MibScalar
jnxJsPolicySystemStatsTotalAllowIPv6FlowsRate = _JnxJsPolicySystemStatsTotalAllowIPv6FlowsRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 2, 10),
    _JnxJsPolicySystemStatsTotalAllowIPv6FlowsRate_Type()
)
jnxJsPolicySystemStatsTotalAllowIPv6FlowsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsTotalAllowIPv6FlowsRate.setStatus("current")


class _JnxJsPolicySystemStatsEnabled_Type(Integer32):
    """Custom type jnxJsPolicySystemStatsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_JnxJsPolicySystemStatsEnabled_Type.__name__ = "Integer32"
_JnxJsPolicySystemStatsEnabled_Object = MibScalar
jnxJsPolicySystemStatsEnabled = _JnxJsPolicySystemStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 3, 3),
    _JnxJsPolicySystemStatsEnabled_Type()
)
jnxJsPolicySystemStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsPolicySystemStatsEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-POLICY-MIB",
    **{"jnxJsSecPolicyMIB": jnxJsSecPolicyMIB,
       "jnxJsPolicyNotifications": jnxJsPolicyNotifications,
       "jnxJsPolicyObjects": jnxJsPolicyObjects,
       "jnxJsPolicyNumber": jnxJsPolicyNumber,
       "jnxJsPolicyTable": jnxJsPolicyTable,
       "jnxJsPolicyEntry": jnxJsPolicyEntry,
       "jnxJsPolicyFromZone": jnxJsPolicyFromZone,
       "jnxJsPolicyToZone": jnxJsPolicyToZone,
       "jnxJsPolicyName": jnxJsPolicyName,
       "jnxJsPolicySequenceNumber": jnxJsPolicySequenceNumber,
       "jnxJsPolicyAction": jnxJsPolicyAction,
       "jnxJsPolicyScheduler": jnxJsPolicyScheduler,
       "jnxJsPolicyState": jnxJsPolicyState,
       "jnxJsPolicyStatsAvailability": jnxJsPolicyStatsAvailability,
       "jnxJsPolicyPerSecBytesThreshold": jnxJsPolicyPerSecBytesThreshold,
       "jnxJsPolicyPerMinKbytesThreshold": jnxJsPolicyPerMinKbytesThreshold,
       "jnxJsPolicyStatsTable": jnxJsPolicyStatsTable,
       "jnxJsPolicyStatsEntry": jnxJsPolicyStatsEntry,
       "jnxJsPolicyStatsCreationTime": jnxJsPolicyStatsCreationTime,
       "jnxJsPolicyStatsInputBytes": jnxJsPolicyStatsInputBytes,
       "jnxJsPolicyStatsInputByteRate": jnxJsPolicyStatsInputByteRate,
       "jnxJsPolicyStatsOutputBytes": jnxJsPolicyStatsOutputBytes,
       "jnxJsPolicyStatsOutputByteRate": jnxJsPolicyStatsOutputByteRate,
       "jnxJsPolicyStatsInputPackets": jnxJsPolicyStatsInputPackets,
       "jnxJsPolicyStatsInputPacketRate": jnxJsPolicyStatsInputPacketRate,
       "jnxJsPolicyStatsOutputPackets": jnxJsPolicyStatsOutputPackets,
       "jnxJsPolicyStatsOutputPacketRate": jnxJsPolicyStatsOutputPacketRate,
       "jnxJsPolicyStatsNumSessions": jnxJsPolicyStatsNumSessions,
       "jnxJsPolicyStatsSessionRate": jnxJsPolicyStatsSessionRate,
       "jnxJsPolicyStatsSessionDeleted": jnxJsPolicyStatsSessionDeleted,
       "jnxJsPolicyStatsLookups": jnxJsPolicyStatsLookups,
       "jnxJsPolicyStatsCountAlarm": jnxJsPolicyStatsCountAlarm,
       "jnxJsPolicyStatsInBytesInit": jnxJsPolicyStatsInBytesInit,
       "jnxJsPolicyStatsInBytesRep": jnxJsPolicyStatsInBytesRep,
       "jnxJsPolicyStatsInByteRtInit": jnxJsPolicyStatsInByteRtInit,
       "jnxJsPolicyStatsInByteRtRep": jnxJsPolicyStatsInByteRtRep,
       "jnxJsPolicyStatsOutBytesInit": jnxJsPolicyStatsOutBytesInit,
       "jnxJsPolicyStatsOutBytesRep": jnxJsPolicyStatsOutBytesRep,
       "jnxJsPolicyStatsOutByteRtInit": jnxJsPolicyStatsOutByteRtInit,
       "jnxJsPolicyStatsOutByteRtRep": jnxJsPolicyStatsOutByteRtRep,
       "jnxJsPolicyStatsInPacketsInit": jnxJsPolicyStatsInPacketsInit,
       "jnxJsPolicyStatsInPacketsRep": jnxJsPolicyStatsInPacketsRep,
       "jnxJsPolicyStatsInPacketRtInit": jnxJsPolicyStatsInPacketRtInit,
       "jnxJsPolicyStatsInPacketRtRep": jnxJsPolicyStatsInPacketRtRep,
       "jnxJsPolicyStatsOutPacketsInit": jnxJsPolicyStatsOutPacketsInit,
       "jnxJsPolicyStatsOutPacketsRep": jnxJsPolicyStatsOutPacketsRep,
       "jnxJsPolicyStatsOutPacketRtInit": jnxJsPolicyStatsOutPacketRtInit,
       "jnxJsPolicyStatsOutPacketRtRep": jnxJsPolicyStatsOutPacketRtRep,
       "jnxJsPolicyTrapVars": jnxJsPolicyTrapVars,
       "jnxJsPolicySystemStats": jnxJsPolicySystemStats,
       "jnxJsPolicySystemStatsIPv4": jnxJsPolicySystemStatsIPv4,
       "jnxJsPolicySystemStatsTotalAllowIPv4Packets": jnxJsPolicySystemStatsTotalAllowIPv4Packets,
       "jnxJsPolicySystemStatsTotalAllowIPv4Bytes": jnxJsPolicySystemStatsTotalAllowIPv4Bytes,
       "jnxJsPolicySystemStatsTotalAllowIPv4PacketsRate": jnxJsPolicySystemStatsTotalAllowIPv4PacketsRate,
       "jnxJsPolicySystemStatsTotalAllowIPv4BytesRate": jnxJsPolicySystemStatsTotalAllowIPv4BytesRate,
       "jnxJsPolicySystemStatsTotalDropIPv4Packets": jnxJsPolicySystemStatsTotalDropIPv4Packets,
       "jnxJsPolicySystemStatsTotalDropIPv4Bytes": jnxJsPolicySystemStatsTotalDropIPv4Bytes,
       "jnxJsPolicySystemStatsTotalDropIPv4PacketsRate": jnxJsPolicySystemStatsTotalDropIPv4PacketsRate,
       "jnxJsPolicySystemStatsTotalDropIPv4BytesRate": jnxJsPolicySystemStatsTotalDropIPv4BytesRate,
       "jnxJsPolicySystemStatsTotalAllowIPv4Flows": jnxJsPolicySystemStatsTotalAllowIPv4Flows,
       "jnxJsPolicySystemStatsTotalAllowIPv4FlowsRate": jnxJsPolicySystemStatsTotalAllowIPv4FlowsRate,
       "jnxJsPolicySystemStatsIPv6": jnxJsPolicySystemStatsIPv6,
       "jnxJsPolicySystemStatsTotalAllowIPv6Packets": jnxJsPolicySystemStatsTotalAllowIPv6Packets,
       "jnxJsPolicySystemStatsTotalAllowIPv6Bytes": jnxJsPolicySystemStatsTotalAllowIPv6Bytes,
       "jnxJsPolicySystemStatsTotalAllowIPv6PacketsRate": jnxJsPolicySystemStatsTotalAllowIPv6PacketsRate,
       "jnxJsPolicySystemStatsTotalAllowIPv6BytesRate": jnxJsPolicySystemStatsTotalAllowIPv6BytesRate,
       "jnxJsPolicySystemStatsTotalDropIPv6Packets": jnxJsPolicySystemStatsTotalDropIPv6Packets,
       "jnxJsPolicySystemStatsTotalDropIPv6Bytes": jnxJsPolicySystemStatsTotalDropIPv6Bytes,
       "jnxJsPolicySystemStatsTotalDropIPv6PacketsRate": jnxJsPolicySystemStatsTotalDropIPv6PacketsRate,
       "jnxJsPolicySystemStatsTotalDropIPv6BytesRate": jnxJsPolicySystemStatsTotalDropIPv6BytesRate,
       "jnxJsPolicySystemStatsTotalAllowIPv6Flows": jnxJsPolicySystemStatsTotalAllowIPv6Flows,
       "jnxJsPolicySystemStatsTotalAllowIPv6FlowsRate": jnxJsPolicySystemStatsTotalAllowIPv6FlowsRate,
       "jnxJsPolicySystemStatsEnabled": jnxJsPolicySystemStatsEnabled}
)
