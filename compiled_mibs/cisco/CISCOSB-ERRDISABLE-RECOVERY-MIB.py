# SNMP MIB module (CISCOSB-ERRDISABLE-RECOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:41 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlErrdisableRecovery = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128)
)
if mibBuilder.loadTexts:
    rlErrdisableRecovery.setRevisions(
        ("2007-11-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("loopback-detection", 1),
          ("port-security", 2),
          ("dot1x-src-address", 3),
          ("acl-deny", 4),
          ("stp-bpdu-guard", 5),
          ("stp-loopback-guard", 6),
          ("pcb-overheat", 7),
          ("udld", 8),
          ("storm-control", 9),
          ("link-flapping", 10))
    )



# MIB Managed Objects in the order of their OIDs



class _RlErrdisableRecoveryInterval_Type(Integer32):
    """Custom type rlErrdisableRecoveryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_RlErrdisableRecoveryInterval_Type.__name__ = "Integer32"
_RlErrdisableRecoveryInterval_Object = MibScalar
rlErrdisableRecoveryInterval = _RlErrdisableRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 1),
    _RlErrdisableRecoveryInterval_Type()
)
rlErrdisableRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryInterval.setUnits("seconds")
_RlErrdisableRecoveryCauseTable_Object = MibTable
rlErrdisableRecoveryCauseTable = _RlErrdisableRecoveryCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2)
)
if mibBuilder.loadTexts:
    rlErrdisableRecoveryCauseTable.setStatus("current")
_RlErrdisableRecoveryCauseEntry_Object = MibTableRow
rlErrdisableRecoveryCauseEntry = _RlErrdisableRecoveryCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1)
)
rlErrdisableRecoveryCauseEntry.setIndexNames(
    (0, "CISCOSB-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"),
)
if mibBuilder.loadTexts:
    rlErrdisableRecoveryCauseEntry.setStatus("current")
_RlErrdisableRecoveryCause_Type = RlErrdisableRecoveryCauseType
_RlErrdisableRecoveryCause_Object = MibTableColumn
rlErrdisableRecoveryCause = _RlErrdisableRecoveryCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 1),
    _RlErrdisableRecoveryCause_Type()
)
rlErrdisableRecoveryCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryCause.setStatus("current")
_RlErrdisableRecoveryEnable_Type = TruthValue
_RlErrdisableRecoveryEnable_Object = MibTableColumn
rlErrdisableRecoveryEnable = _RlErrdisableRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 2),
    _RlErrdisableRecoveryEnable_Type()
)
rlErrdisableRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryEnable.setStatus("current")
_RlErrdisableRecoveryIfTable_Object = MibTable
rlErrdisableRecoveryIfTable = _RlErrdisableRecoveryIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3)
)
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfTable.setStatus("current")
_RlErrdisableRecoveryIfEntry_Object = MibTableRow
rlErrdisableRecoveryIfEntry = _RlErrdisableRecoveryIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1)
)
rlErrdisableRecoveryIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfEntry.setStatus("current")
_RlErrdisableRecoveryIfReason_Type = RlErrdisableRecoveryCauseType
_RlErrdisableRecoveryIfReason_Object = MibTableColumn
rlErrdisableRecoveryIfReason = _RlErrdisableRecoveryIfReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 1),
    _RlErrdisableRecoveryIfReason_Type()
)
rlErrdisableRecoveryIfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfReason.setStatus("current")
_RlErrdisableRecoveryIfEnable_Type = TruthValue
_RlErrdisableRecoveryIfEnable_Object = MibTableColumn
rlErrdisableRecoveryIfEnable = _RlErrdisableRecoveryIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 2),
    _RlErrdisableRecoveryIfEnable_Type()
)
rlErrdisableRecoveryIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfEnable.setStatus("current")
_RlErrdisableRecoveryIfTimeToRecover_Type = Integer32
_RlErrdisableRecoveryIfTimeToRecover_Object = MibTableColumn
rlErrdisableRecoveryIfTimeToRecover = _RlErrdisableRecoveryIfTimeToRecover_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 3),
    _RlErrdisableRecoveryIfTimeToRecover_Type()
)
rlErrdisableRecoveryIfTimeToRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfTimeToRecover.setStatus("current")
if mibBuilder.loadTexts:
    rlErrdisableRecoveryIfTimeToRecover.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ERRDISABLE-RECOVERY-MIB",
    **{"RlErrdisableRecoveryCauseType": RlErrdisableRecoveryCauseType,
       "rlErrdisableRecovery": rlErrdisableRecovery,
       "rlErrdisableRecoveryInterval": rlErrdisableRecoveryInterval,
       "rlErrdisableRecoveryCauseTable": rlErrdisableRecoveryCauseTable,
       "rlErrdisableRecoveryCauseEntry": rlErrdisableRecoveryCauseEntry,
       "rlErrdisableRecoveryCause": rlErrdisableRecoveryCause,
       "rlErrdisableRecoveryEnable": rlErrdisableRecoveryEnable,
       "rlErrdisableRecoveryIfTable": rlErrdisableRecoveryIfTable,
       "rlErrdisableRecoveryIfEntry": rlErrdisableRecoveryIfEntry,
       "rlErrdisableRecoveryIfReason": rlErrdisableRecoveryIfReason,
       "rlErrdisableRecoveryIfEnable": rlErrdisableRecoveryIfEnable,
       "rlErrdisableRecoveryIfTimeToRecover": rlErrdisableRecoveryIfTimeToRecover}
)
