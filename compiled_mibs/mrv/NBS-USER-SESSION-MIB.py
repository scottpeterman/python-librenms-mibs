# SNMP MIB module (NBS-USER-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-USER-SESSION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:39 2025
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

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsUserSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 218)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsUserSessionGrp_ObjectIdentity = ObjectIdentity
nbsUserSessionGrp = _NbsUserSessionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 218, 1)
)
if mibBuilder.loadTexts:
    nbsUserSessionGrp.setStatus("current")
_NbsUserSessionTableSize_Type = Integer32
_NbsUserSessionTableSize_Object = MibScalar
nbsUserSessionTableSize = _NbsUserSessionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 1),
    _NbsUserSessionTableSize_Type()
)
nbsUserSessionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionTableSize.setStatus("current")
_NbsUserSessionTable_Object = MibTable
nbsUserSessionTable = _NbsUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2)
)
if mibBuilder.loadTexts:
    nbsUserSessionTable.setStatus("current")
_NbsUserSessionEntry_Object = MibTableRow
nbsUserSessionEntry = _NbsUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1)
)
nbsUserSessionEntry.setIndexNames(
    (0, "NBS-USER-SESSION-MIB", "nbsUserSessionPID"),
)
if mibBuilder.loadTexts:
    nbsUserSessionEntry.setStatus("current")
_NbsUserSessionPID_Type = Unsigned32
_NbsUserSessionPID_Object = MibTableColumn
nbsUserSessionPID = _NbsUserSessionPID_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 1),
    _NbsUserSessionPID_Type()
)
nbsUserSessionPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsUserSessionPID.setStatus("current")
_NbsUserSessionRowStatus_Type = RowStatus
_NbsUserSessionRowStatus_Object = MibTableColumn
nbsUserSessionRowStatus = _NbsUserSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 2),
    _NbsUserSessionRowStatus_Type()
)
nbsUserSessionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsUserSessionRowStatus.setStatus("current")


class _NbsUserSessionType_Type(Integer32):
    """Custom type nbsUserSessionType based on Integer32"""
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
        *(("runLvl", 1),
          ("bootTime", 2),
          ("newTime", 3),
          ("oldTime", 4),
          ("initProcess", 5),
          ("loginProcess", 6),
          ("userProcess", 7),
          ("deadProcess", 8),
          ("accounting", 9))
    )


_NbsUserSessionType_Type.__name__ = "Integer32"
_NbsUserSessionType_Object = MibTableColumn
nbsUserSessionType = _NbsUserSessionType_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 3),
    _NbsUserSessionType_Type()
)
nbsUserSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionType.setStatus("current")


class _NbsUserSessionLine_Type(DisplayString):
    """Custom type nbsUserSessionLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsUserSessionLine_Type.__name__ = "DisplayString"
_NbsUserSessionLine_Object = MibTableColumn
nbsUserSessionLine = _NbsUserSessionLine_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 4),
    _NbsUserSessionLine_Type()
)
nbsUserSessionLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionLine.setStatus("current")


class _NbsUserSessionId_Type(DisplayString):
    """Custom type nbsUserSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_NbsUserSessionId_Type.__name__ = "DisplayString"
_NbsUserSessionId_Object = MibTableColumn
nbsUserSessionId = _NbsUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 5),
    _NbsUserSessionId_Type()
)
nbsUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionId.setStatus("current")


class _NbsUserSessionUser_Type(DisplayString):
    """Custom type nbsUserSessionUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsUserSessionUser_Type.__name__ = "DisplayString"
_NbsUserSessionUser_Object = MibTableColumn
nbsUserSessionUser = _NbsUserSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 6),
    _NbsUserSessionUser_Type()
)
nbsUserSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionUser.setStatus("current")


class _NbsUserSessionHost_Type(DisplayString):
    """Custom type nbsUserSessionHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsUserSessionHost_Type.__name__ = "DisplayString"
_NbsUserSessionHost_Object = MibTableColumn
nbsUserSessionHost = _NbsUserSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 7),
    _NbsUserSessionHost_Type()
)
nbsUserSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionHost.setStatus("current")
_NbsUserSessionConnectTime_Type = Unsigned32
_NbsUserSessionConnectTime_Object = MibTableColumn
nbsUserSessionConnectTime = _NbsUserSessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 8),
    _NbsUserSessionConnectTime_Type()
)
nbsUserSessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionConnectTime.setStatus("current")


class _NbsUserSessionVia_Type(Integer32):
    """Custom type nbsUserSessionVia based on Integer32"""
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
        *(("notSupported", 0),
          ("console", 1),
          ("ssh", 2),
          ("telnet", 3),
          ("api", 4),
          ("snmp", 5),
          ("gui", 6))
    )


_NbsUserSessionVia_Type.__name__ = "Integer32"
_NbsUserSessionVia_Object = MibTableColumn
nbsUserSessionVia = _NbsUserSessionVia_Object(
    (1, 3, 6, 1, 4, 1, 629, 218, 1, 2, 1, 9),
    _NbsUserSessionVia_Type()
)
nbsUserSessionVia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUserSessionVia.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-USER-SESSION-MIB",
    **{"nbsUserSessionMib": nbsUserSessionMib,
       "nbsUserSessionGrp": nbsUserSessionGrp,
       "nbsUserSessionTableSize": nbsUserSessionTableSize,
       "nbsUserSessionTable": nbsUserSessionTable,
       "nbsUserSessionEntry": nbsUserSessionEntry,
       "nbsUserSessionPID": nbsUserSessionPID,
       "nbsUserSessionRowStatus": nbsUserSessionRowStatus,
       "nbsUserSessionType": nbsUserSessionType,
       "nbsUserSessionLine": nbsUserSessionLine,
       "nbsUserSessionId": nbsUserSessionId,
       "nbsUserSessionUser": nbsUserSessionUser,
       "nbsUserSessionHost": nbsUserSessionHost,
       "nbsUserSessionConnectTime": nbsUserSessionConnectTime,
       "nbsUserSessionVia": nbsUserSessionVia}
)
