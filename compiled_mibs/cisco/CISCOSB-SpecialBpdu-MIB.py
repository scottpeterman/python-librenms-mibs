# SNMP MIB module (CISCOSB-SpecialBpdu-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-SpecialBpdu-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:54 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSpecialBpdu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144)
)
if mibBuilder.loadTexts:
    rlSpecialBpdu.setRevisions(
        ("2008-05-03 12:34",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EncapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ethernet-v2", 2),
          ("llc", 3),
          ("llc-snap", 4))
    )



class Action(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("discard", 2))
    )



class HwAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("drop", 2),
          ("trap", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlSpecialBpduTable_Object = MibTable
rlSpecialBpduTable = _RlSpecialBpduTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1)
)
if mibBuilder.loadTexts:
    rlSpecialBpduTable.setStatus("current")
_RlSpecialBpduEntry_Object = MibTableRow
rlSpecialBpduEntry = _RlSpecialBpduEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1)
)
rlSpecialBpduEntry.setIndexNames(
    (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"),
    (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduEncap"),
    (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduProtId"),
)
if mibBuilder.loadTexts:
    rlSpecialBpduEntry.setStatus("current")
_RlSpecialBpduMacAddr_Type = MacAddress
_RlSpecialBpduMacAddr_Object = MibTableColumn
rlSpecialBpduMacAddr = _RlSpecialBpduMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 1),
    _RlSpecialBpduMacAddr_Type()
)
rlSpecialBpduMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpecialBpduMacAddr.setStatus("current")
_RlSpecialBpduEncap_Type = EncapType
_RlSpecialBpduEncap_Object = MibTableColumn
rlSpecialBpduEncap = _RlSpecialBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 2),
    _RlSpecialBpduEncap_Type()
)
rlSpecialBpduEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpecialBpduEncap.setStatus("current")


class _RlSpecialBpduProtId_Type(OctetString):
    """Custom type rlSpecialBpduProtId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_RlSpecialBpduProtId_Type.__name__ = "OctetString"
_RlSpecialBpduProtId_Object = MibTableColumn
rlSpecialBpduProtId = _RlSpecialBpduProtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 3),
    _RlSpecialBpduProtId_Type()
)
rlSpecialBpduProtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSpecialBpduProtId.setStatus("current")
_RlSpecialBpduAction_Type = Action
_RlSpecialBpduAction_Object = MibTableColumn
rlSpecialBpduAction = _RlSpecialBpduAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 4),
    _RlSpecialBpduAction_Type()
)
rlSpecialBpduAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSpecialBpduAction.setStatus("current")
_RlSpecialBpduRowStatus_Type = RowStatus
_RlSpecialBpduRowStatus_Object = MibTableColumn
rlSpecialBpduRowStatus = _RlSpecialBpduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 5),
    _RlSpecialBpduRowStatus_Type()
)
rlSpecialBpduRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSpecialBpduRowStatus.setStatus("current")
_RlSpecialBpduHwTable_Object = MibTable
rlSpecialBpduHwTable = _RlSpecialBpduHwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2)
)
if mibBuilder.loadTexts:
    rlSpecialBpduHwTable.setStatus("current")
_RlSpecialBpduHwEntry_Object = MibTableRow
rlSpecialBpduHwEntry = _RlSpecialBpduHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1)
)
rlSpecialBpduHwEntry.setIndexNames(
    (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"),
)
if mibBuilder.loadTexts:
    rlSpecialBpduHwEntry.setStatus("current")
_RlSpecialBpduHwAction_Type = HwAction
_RlSpecialBpduHwAction_Object = MibTableColumn
rlSpecialBpduHwAction = _RlSpecialBpduHwAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1, 2),
    _RlSpecialBpduHwAction_Type()
)
rlSpecialBpduHwAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSpecialBpduHwAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SpecialBpdu-MIB",
    **{"EncapType": EncapType,
       "Action": Action,
       "HwAction": HwAction,
       "rlSpecialBpdu": rlSpecialBpdu,
       "rlSpecialBpduTable": rlSpecialBpduTable,
       "rlSpecialBpduEntry": rlSpecialBpduEntry,
       "rlSpecialBpduMacAddr": rlSpecialBpduMacAddr,
       "rlSpecialBpduEncap": rlSpecialBpduEncap,
       "rlSpecialBpduProtId": rlSpecialBpduProtId,
       "rlSpecialBpduAction": rlSpecialBpduAction,
       "rlSpecialBpduRowStatus": rlSpecialBpduRowStatus,
       "rlSpecialBpduHwTable": rlSpecialBpduHwTable,
       "rlSpecialBpduHwEntry": rlSpecialBpduHwEntry,
       "rlSpecialBpduHwAction": rlSpecialBpduHwAction}
)
