# SNMP MIB module (CISCOSB-TIMEBASED-PORT-SHUTDOWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-TIMEBASED-PORT-SHUTDOWN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:01 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

rlTimeBasedPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208)
)
if mibBuilder.loadTexts:
    rlTimeBasedPort.setRevisions(
        ("2011-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlTimeBasedPortVersion_Type = Integer32
_RlTimeBasedPortVersion_Object = MibScalar
rlTimeBasedPortVersion = _RlTimeBasedPortVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 1),
    _RlTimeBasedPortVersion_Type()
)
rlTimeBasedPortVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeBasedPortVersion.setStatus("current")
_RlTimeBasedPortTable_Object = MibTable
rlTimeBasedPortTable = _RlTimeBasedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2)
)
if mibBuilder.loadTexts:
    rlTimeBasedPortTable.setStatus("current")
_RlTimeBasedPortEntry_Object = MibTableRow
rlTimeBasedPortEntry = _RlTimeBasedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2, 1)
)
rlTimeBasedPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCOSB-TIMEBASED-PORT-SHUTDOWN-MIB", "rlTimeBasedPortTimeRangeName"),
)
if mibBuilder.loadTexts:
    rlTimeBasedPortEntry.setStatus("current")


class _RlTimeBasedPortTimeRangeName_Type(DisplayString):
    """Custom type rlTimeBasedPortTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlTimeBasedPortTimeRangeName_Type.__name__ = "DisplayString"
_RlTimeBasedPortTimeRangeName_Object = MibTableColumn
rlTimeBasedPortTimeRangeName = _RlTimeBasedPortTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2, 1, 1),
    _RlTimeBasedPortTimeRangeName_Type()
)
rlTimeBasedPortTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTimeBasedPortTimeRangeName.setStatus("current")


class _RlTimeBasedPortAction_Type(Integer32):
    """Custom type rlTimeBasedPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RlTimeBasedPortAction_Type.__name__ = "Integer32"
_RlTimeBasedPortAction_Object = MibTableColumn
rlTimeBasedPortAction = _RlTimeBasedPortAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2, 1, 2),
    _RlTimeBasedPortAction_Type()
)
rlTimeBasedPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeBasedPortAction.setStatus("current")
_RlTimeBasedPortActive_Type = TruthValue
_RlTimeBasedPortActive_Object = MibTableColumn
rlTimeBasedPortActive = _RlTimeBasedPortActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2, 1, 3),
    _RlTimeBasedPortActive_Type()
)
rlTimeBasedPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeBasedPortActive.setStatus("current")
_RlTimeBasedPortRowStatus_Type = RowStatus
_RlTimeBasedPortRowStatus_Object = MibTableColumn
rlTimeBasedPortRowStatus = _RlTimeBasedPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208, 2, 1, 4),
    _RlTimeBasedPortRowStatus_Type()
)
rlTimeBasedPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeBasedPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-TIMEBASED-PORT-SHUTDOWN-MIB",
    **{"rlTimeBasedPort": rlTimeBasedPort,
       "rlTimeBasedPortVersion": rlTimeBasedPortVersion,
       "rlTimeBasedPortTable": rlTimeBasedPortTable,
       "rlTimeBasedPortEntry": rlTimeBasedPortEntry,
       "rlTimeBasedPortTimeRangeName": rlTimeBasedPortTimeRangeName,
       "rlTimeBasedPortAction": rlTimeBasedPortAction,
       "rlTimeBasedPortActive": rlTimeBasedPortActive,
       "rlTimeBasedPortRowStatus": rlTimeBasedPortRowStatus}
)
