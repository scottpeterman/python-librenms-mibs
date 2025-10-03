# SNMP MIB module (CISCOSB-SOCKET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SOCKET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:52 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rlSocket = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85)
)
if mibBuilder.loadTexts:
    rlSocket.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlSocketMibVersion_Type = Integer32
_RlSocketMibVersion_Object = MibScalar
rlSocketMibVersion = _RlSocketMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 1),
    _RlSocketMibVersion_Type()
)
rlSocketMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketMibVersion.setStatus("current")
_RlSocketTable_Object = MibTable
rlSocketTable = _RlSocketTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2)
)
if mibBuilder.loadTexts:
    rlSocketTable.setStatus("current")
_RlSocketEntry_Object = MibTableRow
rlSocketEntry = _RlSocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1)
)
rlSocketEntry.setIndexNames(
    (0, "CISCOSB-SOCKET-MIB", "rlSocketId"),
)
if mibBuilder.loadTexts:
    rlSocketEntry.setStatus("current")
_RlSocketId_Type = Integer32
_RlSocketId_Object = MibTableColumn
rlSocketId = _RlSocketId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1, 1),
    _RlSocketId_Type()
)
rlSocketId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketId.setStatus("current")


class _RlSocketType_Type(Integer32):
    """Custom type rlSocketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stream", 1),
          ("dgram", 2),
          ("raw", 3))
    )


_RlSocketType_Type.__name__ = "Integer32"
_RlSocketType_Object = MibTableColumn
rlSocketType = _RlSocketType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1, 2),
    _RlSocketType_Type()
)
rlSocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketType.setStatus("current")


class _RlSocketState_Type(Integer32):
    """Custom type rlSocketState based on Integer32"""
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
        *(("connected", 1),
          ("notConnected", 2),
          ("recvClosed", 3),
          ("sendClosed", 4),
          ("closed", 5))
    )


_RlSocketState_Type.__name__ = "Integer32"
_RlSocketState_Object = MibTableColumn
rlSocketState = _RlSocketState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1, 3),
    _RlSocketState_Type()
)
rlSocketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketState.setStatus("current")


class _RlSocketBlockMode_Type(Integer32):
    """Custom type rlSocketBlockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("nonBlocking", 2))
    )


_RlSocketBlockMode_Type.__name__ = "Integer32"
_RlSocketBlockMode_Object = MibTableColumn
rlSocketBlockMode = _RlSocketBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1, 4),
    _RlSocketBlockMode_Type()
)
rlSocketBlockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketBlockMode.setStatus("current")
_RlSocketUpTime_Type = TimeTicks
_RlSocketUpTime_Object = MibTableColumn
rlSocketUpTime = _RlSocketUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85, 2, 1, 5),
    _RlSocketUpTime_Type()
)
rlSocketUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSocketUpTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SOCKET-MIB",
    **{"rlSocket": rlSocket,
       "rlSocketMibVersion": rlSocketMibVersion,
       "rlSocketTable": rlSocketTable,
       "rlSocketEntry": rlSocketEntry,
       "rlSocketId": rlSocketId,
       "rlSocketType": rlSocketType,
       "rlSocketState": rlSocketState,
       "rlSocketBlockMode": rlSocketBlockMode,
       "rlSocketUpTime": rlSocketUpTime}
)
