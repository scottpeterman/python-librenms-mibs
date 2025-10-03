# SNMP MIB module (CIENA-CES-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-TWAMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:57 2025
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

(cienaCesConfig,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig")

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

cienaCesTwampMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33)
)
if mibBuilder.loadTexts:
    cienaCesTwampMIB.setRevisions(
        ("2017-06-07 00:00",
         "2013-11-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesTwampMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesTwampMIBObjects = _CienaCesTwampMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1)
)
_CienaCesTwamp_ObjectIdentity = ObjectIdentity
cienaCesTwamp = _CienaCesTwamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1)
)
_CienaCesTwampModule_ObjectIdentity = ObjectIdentity
cienaCesTwampModule = _CienaCesTwampModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1)
)


class _CienaCesTwampPort_Type(Integer32):
    """Custom type cienaCesTwampPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_CienaCesTwampPort_Type.__name__ = "Integer32"
_CienaCesTwampPort_Object = MibScalar
cienaCesTwampPort = _CienaCesTwampPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 1),
    _CienaCesTwampPort_Type()
)
cienaCesTwampPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampPort.setStatus("current")


class _CienaCesTwampEnable_Type(Integer32):
    """Custom type cienaCesTwampEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CienaCesTwampEnable_Type.__name__ = "Integer32"
_CienaCesTwampEnable_Object = MibScalar
cienaCesTwampEnable = _CienaCesTwampEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 2),
    _CienaCesTwampEnable_Type()
)
cienaCesTwampEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampEnable.setStatus("current")


class _CienaCesTwampServerEnable_Type(Integer32):
    """Custom type cienaCesTwampServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CienaCesTwampServerEnable_Type.__name__ = "Integer32"
_CienaCesTwampServerEnable_Object = MibScalar
cienaCesTwampServerEnable = _CienaCesTwampServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 3),
    _CienaCesTwampServerEnable_Type()
)
cienaCesTwampServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerEnable.setStatus("current")
_CienaCesTwampServerSessionsTable_Object = MibTable
cienaCesTwampServerSessionsTable = _CienaCesTwampServerSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionsTable.setStatus("current")
_CienaCesTwampServerSessionEntry_Object = MibTableRow
cienaCesTwampServerSessionEntry = _CienaCesTwampServerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1)
)
cienaCesTwampServerSessionEntry.setIndexNames(
    (0, "CIENA-CES-TWAMP-MIB", "cienaCesTwampServerSessionId"),
)
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionEntry.setStatus("current")


class _CienaCesTwampServerSessionId_Type(Integer32):
    """Custom type cienaCesTwampServerSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesTwampServerSessionId_Type.__name__ = "Integer32"
_CienaCesTwampServerSessionId_Object = MibTableColumn
cienaCesTwampServerSessionId = _CienaCesTwampServerSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 1),
    _CienaCesTwampServerSessionId_Type()
)
cienaCesTwampServerSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionId.setStatus("current")


class _CienaCesTwampServerSessionState_Type(Integer32):
    """Custom type cienaCesTwampServerSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("listen", 0),
          ("greet", 1),
          ("start", 2),
          ("accept", 3),
          ("test", 4),
          ("stop", 5),
          ("error", 6))
    )


_CienaCesTwampServerSessionState_Type.__name__ = "Integer32"
_CienaCesTwampServerSessionState_Object = MibTableColumn
cienaCesTwampServerSessionState = _CienaCesTwampServerSessionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 2),
    _CienaCesTwampServerSessionState_Type()
)
cienaCesTwampServerSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionState.setStatus("current")


class _CienaCesTwampServerSessionPort_Type(Integer32):
    """Custom type cienaCesTwampServerSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTwampServerSessionPort_Type.__name__ = "Integer32"
_CienaCesTwampServerSessionPort_Object = MibTableColumn
cienaCesTwampServerSessionPort = _CienaCesTwampServerSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 3),
    _CienaCesTwampServerSessionPort_Type()
)
cienaCesTwampServerSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionPort.setStatus("current")
_CienaCesTwampServerSessionHost_Type = IpAddress
_CienaCesTwampServerSessionHost_Object = MibTableColumn
cienaCesTwampServerSessionHost = _CienaCesTwampServerSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 4),
    _CienaCesTwampServerSessionHost_Type()
)
cienaCesTwampServerSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionHost.setStatus("current")
_CienaCesTwampServerSessionNumPkts_Type = Integer32
_CienaCesTwampServerSessionNumPkts_Object = MibTableColumn
cienaCesTwampServerSessionNumPkts = _CienaCesTwampServerSessionNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 5),
    _CienaCesTwampServerSessionNumPkts_Type()
)
cienaCesTwampServerSessionNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionNumPkts.setStatus("current")
_CienaCesTwampServerSessionSeqNum_Type = Integer32
_CienaCesTwampServerSessionSeqNum_Object = MibTableColumn
cienaCesTwampServerSessionSeqNum = _CienaCesTwampServerSessionSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 4, 1, 6),
    _CienaCesTwampServerSessionSeqNum_Type()
)
cienaCesTwampServerSessionSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerSessionSeqNum.setStatus("current")


class _CienaCesTwampTimeout_Type(Integer32):
    """Custom type cienaCesTwampTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CienaCesTwampTimeout_Type.__name__ = "Integer32"
_CienaCesTwampTimeout_Object = MibScalar
cienaCesTwampTimeout = _CienaCesTwampTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 5),
    _CienaCesTwampTimeout_Type()
)
cienaCesTwampTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampTimeout.setStatus("current")


class _CienaCesTwampServerDscp_Type(Integer32):
    """Custom type cienaCesTwampServerDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesTwampServerDscp_Type.__name__ = "Integer32"
_CienaCesTwampServerDscp_Object = MibScalar
cienaCesTwampServerDscp = _CienaCesTwampServerDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 6),
    _CienaCesTwampServerDscp_Type()
)
cienaCesTwampServerDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerDscp.setStatus("current")
_CienaCesTwampServerCtrlSessionsTable_Object = MibTable
cienaCesTwampServerCtrlSessionsTable = _CienaCesTwampServerCtrlSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionsTable.setStatus("current")
_CienaCesTwampServerCtrlSessionEntry_Object = MibTableRow
cienaCesTwampServerCtrlSessionEntry = _CienaCesTwampServerCtrlSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1)
)
cienaCesTwampServerCtrlSessionEntry.setIndexNames(
    (0, "CIENA-CES-TWAMP-MIB", "cienaCesTwampServerCtrlSessionId"),
)
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionEntry.setStatus("current")


class _CienaCesTwampServerCtrlSessionId_Type(Integer32):
    """Custom type cienaCesTwampServerCtrlSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesTwampServerCtrlSessionId_Type.__name__ = "Integer32"
_CienaCesTwampServerCtrlSessionId_Object = MibTableColumn
cienaCesTwampServerCtrlSessionId = _CienaCesTwampServerCtrlSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1, 1),
    _CienaCesTwampServerCtrlSessionId_Type()
)
cienaCesTwampServerCtrlSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionId.setStatus("current")


class _CienaCesTwampServerCtrlSessionState_Type(Integer32):
    """Custom type cienaCesTwampServerCtrlSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("listen", 0),
          ("greet", 1),
          ("start", 2),
          ("accept", 3),
          ("test", 4),
          ("stop", 5),
          ("error", 6))
    )


_CienaCesTwampServerCtrlSessionState_Type.__name__ = "Integer32"
_CienaCesTwampServerCtrlSessionState_Object = MibTableColumn
cienaCesTwampServerCtrlSessionState = _CienaCesTwampServerCtrlSessionState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1, 2),
    _CienaCesTwampServerCtrlSessionState_Type()
)
cienaCesTwampServerCtrlSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionState.setStatus("current")


class _CienaCesTwampServerCtrlSessionPort_Type(Integer32):
    """Custom type cienaCesTwampServerCtrlSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesTwampServerCtrlSessionPort_Type.__name__ = "Integer32"
_CienaCesTwampServerCtrlSessionPort_Object = MibTableColumn
cienaCesTwampServerCtrlSessionPort = _CienaCesTwampServerCtrlSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1, 3),
    _CienaCesTwampServerCtrlSessionPort_Type()
)
cienaCesTwampServerCtrlSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionPort.setStatus("current")
_CienaCesTwampServerCtrlSessionHost_Type = IpAddress
_CienaCesTwampServerCtrlSessionHost_Object = MibTableColumn
cienaCesTwampServerCtrlSessionHost = _CienaCesTwampServerCtrlSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1, 4),
    _CienaCesTwampServerCtrlSessionHost_Type()
)
cienaCesTwampServerCtrlSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionHost.setStatus("current")
_CienaCesTwampServerCtrlSessionTestMap_Type = Unsigned32
_CienaCesTwampServerCtrlSessionTestMap_Object = MibTableColumn
cienaCesTwampServerCtrlSessionTestMap = _CienaCesTwampServerCtrlSessionTestMap_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 33, 1, 1, 1, 7, 1, 5),
    _CienaCesTwampServerCtrlSessionTestMap_Type()
)
cienaCesTwampServerCtrlSessionTestMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesTwampServerCtrlSessionTestMap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-TWAMP-MIB",
    **{"cienaCesTwampMIB": cienaCesTwampMIB,
       "cienaCesTwampMIBObjects": cienaCesTwampMIBObjects,
       "cienaCesTwamp": cienaCesTwamp,
       "cienaCesTwampModule": cienaCesTwampModule,
       "cienaCesTwampPort": cienaCesTwampPort,
       "cienaCesTwampEnable": cienaCesTwampEnable,
       "cienaCesTwampServerEnable": cienaCesTwampServerEnable,
       "cienaCesTwampServerSessionsTable": cienaCesTwampServerSessionsTable,
       "cienaCesTwampServerSessionEntry": cienaCesTwampServerSessionEntry,
       "cienaCesTwampServerSessionId": cienaCesTwampServerSessionId,
       "cienaCesTwampServerSessionState": cienaCesTwampServerSessionState,
       "cienaCesTwampServerSessionPort": cienaCesTwampServerSessionPort,
       "cienaCesTwampServerSessionHost": cienaCesTwampServerSessionHost,
       "cienaCesTwampServerSessionNumPkts": cienaCesTwampServerSessionNumPkts,
       "cienaCesTwampServerSessionSeqNum": cienaCesTwampServerSessionSeqNum,
       "cienaCesTwampTimeout": cienaCesTwampTimeout,
       "cienaCesTwampServerDscp": cienaCesTwampServerDscp,
       "cienaCesTwampServerCtrlSessionsTable": cienaCesTwampServerCtrlSessionsTable,
       "cienaCesTwampServerCtrlSessionEntry": cienaCesTwampServerCtrlSessionEntry,
       "cienaCesTwampServerCtrlSessionId": cienaCesTwampServerCtrlSessionId,
       "cienaCesTwampServerCtrlSessionState": cienaCesTwampServerCtrlSessionState,
       "cienaCesTwampServerCtrlSessionPort": cienaCesTwampServerCtrlSessionPort,
       "cienaCesTwampServerCtrlSessionHost": cienaCesTwampServerCtrlSessionHost,
       "cienaCesTwampServerCtrlSessionTestMap": cienaCesTwampServerCtrlSessionTestMap}
)
