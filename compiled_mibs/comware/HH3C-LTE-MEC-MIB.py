# SNMP MIB module (HH3C-LTE-MEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LTE-MEC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:05 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hh3cLTEMEC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185)
)
if mibBuilder.loadTexts:
    hh3cLTEMEC.setRevisions(
        ("2019-06-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLTEMECObjects_ObjectIdentity = ObjectIdentity
hh3cLTEMECObjects = _Hh3cLTEMECObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1)
)
_Hh3cMecTables_ObjectIdentity = ObjectIdentity
hh3cMecTables = _Hh3cMecTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1)
)
_Hh3cMecIfStatsTable_Object = MibTable
hh3cMecIfStatsTable = _Hh3cMecIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMecIfStatsTable.setStatus("current")
_Hh3cMecIfStatsEntry_Object = MibTableRow
hh3cMecIfStatsEntry = _Hh3cMecIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1)
)
hh3cMecIfStatsEntry.setIndexNames(
    (0, "HH3C-LTE-MEC-MIB", "hh3cMecIfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cMecIfStatsEntry.setStatus("current")
_Hh3cMecIfStatsIfIndex_Type = InterfaceIndex
_Hh3cMecIfStatsIfIndex_Object = MibTableColumn
hh3cMecIfStatsIfIndex = _Hh3cMecIfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 1),
    _Hh3cMecIfStatsIfIndex_Type()
)
hh3cMecIfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMecIfStatsIfIndex.setStatus("current")
_Hh3cMecIfStatsGTPUReceive_Type = Counter64
_Hh3cMecIfStatsGTPUReceive_Object = MibTableColumn
hh3cMecIfStatsGTPUReceive = _Hh3cMecIfStatsGTPUReceive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 2),
    _Hh3cMecIfStatsGTPUReceive_Type()
)
hh3cMecIfStatsGTPUReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsGTPUReceive.setStatus("current")
_Hh3cMecIfStatsGTPUSend_Type = Counter64
_Hh3cMecIfStatsGTPUSend_Object = MibTableColumn
hh3cMecIfStatsGTPUSend = _Hh3cMecIfStatsGTPUSend_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 3),
    _Hh3cMecIfStatsGTPUSend_Type()
)
hh3cMecIfStatsGTPUSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsGTPUSend.setStatus("current")
_Hh3cMecIfStatsSCTPReceive_Type = Counter64
_Hh3cMecIfStatsSCTPReceive_Object = MibTableColumn
hh3cMecIfStatsSCTPReceive = _Hh3cMecIfStatsSCTPReceive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 4),
    _Hh3cMecIfStatsSCTPReceive_Type()
)
hh3cMecIfStatsSCTPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsSCTPReceive.setStatus("current")
_Hh3cMecIfStatsSCTPSend_Type = Counter64
_Hh3cMecIfStatsSCTPSend_Object = MibTableColumn
hh3cMecIfStatsSCTPSend = _Hh3cMecIfStatsSCTPSend_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 5),
    _Hh3cMecIfStatsSCTPSend_Type()
)
hh3cMecIfStatsSCTPSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsSCTPSend.setStatus("current")
_Hh3cMecIfStatsDecap_Type = Counter64
_Hh3cMecIfStatsDecap_Object = MibTableColumn
hh3cMecIfStatsDecap = _Hh3cMecIfStatsDecap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 6),
    _Hh3cMecIfStatsDecap_Type()
)
hh3cMecIfStatsDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsDecap.setStatus("current")
_Hh3cMecIfStatsEncap_Type = Counter64
_Hh3cMecIfStatsEncap_Object = MibTableColumn
hh3cMecIfStatsEncap = _Hh3cMecIfStatsEncap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 1, 1, 7),
    _Hh3cMecIfStatsEncap_Type()
)
hh3cMecIfStatsEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecIfStatsEncap.setStatus("current")
_Hh3cMecErrStatsInfo_ObjectIdentity = ObjectIdentity
hh3cMecErrStatsInfo = _Hh3cMecErrStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2)
)
_Hh3cMecErrBadFormat_Type = Counter64
_Hh3cMecErrBadFormat_Object = MibScalar
hh3cMecErrBadFormat = _Hh3cMecErrBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2, 1),
    _Hh3cMecErrBadFormat_Type()
)
hh3cMecErrBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecErrBadFormat.setStatus("current")
_Hh3cMecErrSend_Type = Counter64
_Hh3cMecErrSend_Object = MibScalar
hh3cMecErrSend = _Hh3cMecErrSend_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2, 2),
    _Hh3cMecErrSend_Type()
)
hh3cMecErrSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecErrSend.setStatus("current")
_Hh3cMecErrOutInterface_Type = Counter64
_Hh3cMecErrOutInterface_Object = MibScalar
hh3cMecErrOutInterface = _Hh3cMecErrOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2, 3),
    _Hh3cMecErrOutInterface_Type()
)
hh3cMecErrOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecErrOutInterface.setStatus("current")
_Hh3cMecErrFraglimit_Type = Counter64
_Hh3cMecErrFraglimit_Object = MibScalar
hh3cMecErrFraglimit = _Hh3cMecErrFraglimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2, 4),
    _Hh3cMecErrFraglimit_Type()
)
hh3cMecErrFraglimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecErrFraglimit.setStatus("current")
_Hh3cMecErrFragAttack_Type = Counter64
_Hh3cMecErrFragAttack_Object = MibScalar
hh3cMecErrFragAttack = _Hh3cMecErrFragAttack_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 1, 1, 2, 5),
    _Hh3cMecErrFragAttack_Type()
)
hh3cMecErrFragAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMecErrFragAttack.setStatus("current")
_Hh3cLTEMECTrapObjects_ObjectIdentity = ObjectIdentity
hh3cLTEMECTrapObjects = _Hh3cLTEMECTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2)
)
_Hh3cMecTrap_ObjectIdentity = ObjectIdentity
hh3cMecTrap = _Hh3cMecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2, 0)
)
_Hh3cMecTrapInfo_ObjectIdentity = ObjectIdentity
hh3cMecTrapInfo = _Hh3cMecTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2, 1)
)
_Hh3cMecTunnelCacheNumber_Type = Integer32
_Hh3cMecTunnelCacheNumber_Object = MibScalar
hh3cMecTunnelCacheNumber = _Hh3cMecTunnelCacheNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2, 1, 1),
    _Hh3cMecTunnelCacheNumber_Type()
)
hh3cMecTunnelCacheNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMecTunnelCacheNumber.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cMecTunnelCacheFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2, 0, 1)
)
hh3cMecTunnelCacheFullTrap.setObjects(
    ("HH3C-LTE-MEC-MIB", "hh3cMecTunnelCacheNumber")
)
if mibBuilder.loadTexts:
    hh3cMecTunnelCacheFullTrap.setStatus(
        "current"
    )

hh3cMecTunnelCacheRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 185, 2, 0, 2)
)
hh3cMecTunnelCacheRecoverTrap.setObjects(
    ("HH3C-LTE-MEC-MIB", "hh3cMecTunnelCacheNumber")
)
if mibBuilder.loadTexts:
    hh3cMecTunnelCacheRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LTE-MEC-MIB",
    **{"hh3cLTEMEC": hh3cLTEMEC,
       "hh3cLTEMECObjects": hh3cLTEMECObjects,
       "hh3cMecTables": hh3cMecTables,
       "hh3cMecIfStatsTable": hh3cMecIfStatsTable,
       "hh3cMecIfStatsEntry": hh3cMecIfStatsEntry,
       "hh3cMecIfStatsIfIndex": hh3cMecIfStatsIfIndex,
       "hh3cMecIfStatsGTPUReceive": hh3cMecIfStatsGTPUReceive,
       "hh3cMecIfStatsGTPUSend": hh3cMecIfStatsGTPUSend,
       "hh3cMecIfStatsSCTPReceive": hh3cMecIfStatsSCTPReceive,
       "hh3cMecIfStatsSCTPSend": hh3cMecIfStatsSCTPSend,
       "hh3cMecIfStatsDecap": hh3cMecIfStatsDecap,
       "hh3cMecIfStatsEncap": hh3cMecIfStatsEncap,
       "hh3cMecErrStatsInfo": hh3cMecErrStatsInfo,
       "hh3cMecErrBadFormat": hh3cMecErrBadFormat,
       "hh3cMecErrSend": hh3cMecErrSend,
       "hh3cMecErrOutInterface": hh3cMecErrOutInterface,
       "hh3cMecErrFraglimit": hh3cMecErrFraglimit,
       "hh3cMecErrFragAttack": hh3cMecErrFragAttack,
       "hh3cLTEMECTrapObjects": hh3cLTEMECTrapObjects,
       "hh3cMecTrap": hh3cMecTrap,
       "hh3cMecTunnelCacheFullTrap": hh3cMecTunnelCacheFullTrap,
       "hh3cMecTunnelCacheRecoverTrap": hh3cMecTunnelCacheRecoverTrap,
       "hh3cMecTrapInfo": hh3cMecTrapInfo,
       "hh3cMecTunnelCacheNumber": hh3cMecTunnelCacheNumber}
)
