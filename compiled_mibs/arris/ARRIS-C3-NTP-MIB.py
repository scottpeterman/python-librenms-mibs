# SNMP MIB module (ARRIS-C3-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-NTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:05 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cmtsC3NTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxNTPObjects_ObjectIdentity = ObjectIdentity
dcxNTPObjects = _DcxNTPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1)
)
_DcxNTPServerTable_Object = MibTable
dcxNTPServerTable = _DcxNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    dcxNTPServerTable.setStatus("current")
_DcxNTPServerEntry_Object = MibTableRow
dcxNTPServerEntry = _DcxNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1)
)
dcxNTPServerEntry.setIndexNames(
    (0, "ARRIS-C3-NTP-MIB", "dcxNTPServerIp"),
)
if mibBuilder.loadTexts:
    dcxNTPServerEntry.setStatus("current")
_DcxNTPServerIp_Type = IpAddress
_DcxNTPServerIp_Object = MibTableColumn
dcxNTPServerIp = _DcxNTPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 1),
    _DcxNTPServerIp_Type()
)
dcxNTPServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxNTPServerIp.setStatus("current")


class _DcxNTPServerInterval_Type(Integer32):
    """Custom type dcxNTPServerInterval based on Integer32"""
    defaultValue = 300


_DcxNTPServerInterval_Type.__name__ = "Integer32"
_DcxNTPServerInterval_Object = MibTableColumn
dcxNTPServerInterval = _DcxNTPServerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 2),
    _DcxNTPServerInterval_Type()
)
dcxNTPServerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxNTPServerInterval.setStatus("current")
_DcxNTPServerSuccess_Type = Counter32
_DcxNTPServerSuccess_Object = MibTableColumn
dcxNTPServerSuccess = _DcxNTPServerSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 3),
    _DcxNTPServerSuccess_Type()
)
dcxNTPServerSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxNTPServerSuccess.setStatus("current")
_DcxNTPServerAttempts_Type = Counter32
_DcxNTPServerAttempts_Object = MibTableColumn
dcxNTPServerAttempts = _DcxNTPServerAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 4),
    _DcxNTPServerAttempts_Type()
)
dcxNTPServerAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxNTPServerAttempts.setStatus("current")
_DcxNTPServerOffset_Type = Integer32
_DcxNTPServerOffset_Object = MibTableColumn
dcxNTPServerOffset = _DcxNTPServerOffset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 5),
    _DcxNTPServerOffset_Type()
)
dcxNTPServerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxNTPServerOffset.setStatus("current")
_DcxNTPServerStatus_Type = RowStatus
_DcxNTPServerStatus_Object = MibTableColumn
dcxNTPServerStatus = _DcxNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 6),
    _DcxNTPServerStatus_Type()
)
dcxNTPServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxNTPServerStatus.setStatus("current")
_DcxNTPMasterServer_Type = IpAddress
_DcxNTPMasterServer_Object = MibScalar
dcxNTPMasterServer = _DcxNTPMasterServer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 2),
    _DcxNTPMasterServer_Type()
)
dcxNTPMasterServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxNTPMasterServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-NTP-MIB",
    **{"cmtsC3NTPMIB": cmtsC3NTPMIB,
       "dcxNTPObjects": dcxNTPObjects,
       "dcxNTPServerTable": dcxNTPServerTable,
       "dcxNTPServerEntry": dcxNTPServerEntry,
       "dcxNTPServerIp": dcxNTPServerIp,
       "dcxNTPServerInterval": dcxNTPServerInterval,
       "dcxNTPServerSuccess": dcxNTPServerSuccess,
       "dcxNTPServerAttempts": dcxNTPServerAttempts,
       "dcxNTPServerOffset": dcxNTPServerOffset,
       "dcxNTPServerStatus": dcxNTPServerStatus,
       "dcxNTPMasterServer": dcxNTPMasterServer}
)
