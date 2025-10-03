# SNMP MIB module (CISCOSB-DIGITALKEYMANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-DIGITALKEYMANAGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:32 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDigitalKeyManage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86)
)
if mibBuilder.loadTexts:
    rlDigitalKeyManage.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlMD5KeyChainTable_Object = MibTable
rlMD5KeyChainTable = _RlMD5KeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1)
)
if mibBuilder.loadTexts:
    rlMD5KeyChainTable.setStatus("current")
_RlMD5KeyChainEntry_Object = MibTableRow
rlMD5KeyChainEntry = _RlMD5KeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1)
)
rlMD5KeyChainEntry.setIndexNames(
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainName"),
    (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainKeyId"),
)
if mibBuilder.loadTexts:
    rlMD5KeyChainEntry.setStatus("current")
_RlMD5KeyChainName_Type = DisplayString
_RlMD5KeyChainName_Object = MibTableColumn
rlMD5KeyChainName = _RlMD5KeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 1),
    _RlMD5KeyChainName_Type()
)
rlMD5KeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainName.setStatus("current")


class _RlMD5KeyChainKeyId_Type(Integer32):
    """Custom type rlMD5KeyChainKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlMD5KeyChainKeyId_Type.__name__ = "Integer32"
_RlMD5KeyChainKeyId_Object = MibTableColumn
rlMD5KeyChainKeyId = _RlMD5KeyChainKeyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 2),
    _RlMD5KeyChainKeyId_Type()
)
rlMD5KeyChainKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyId.setStatus("current")


class _RlMD5KeyChainKey_Type(DisplayString):
    """Custom type rlMD5KeyChainKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlMD5KeyChainKey_Type.__name__ = "DisplayString"
_RlMD5KeyChainKey_Object = MibTableColumn
rlMD5KeyChainKey = _RlMD5KeyChainKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 3),
    _RlMD5KeyChainKey_Type()
)
rlMD5KeyChainKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKey.setStatus("current")
_RlMD5KeyChainKeyStartAccept_Type = DateAndTime
_RlMD5KeyChainKeyStartAccept_Object = MibTableColumn
rlMD5KeyChainKeyStartAccept = _RlMD5KeyChainKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 4),
    _RlMD5KeyChainKeyStartAccept_Type()
)
rlMD5KeyChainKeyStartAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStartAccept.setStatus("current")
_RlMD5KeyChainKeyStartGenerate_Type = DateAndTime
_RlMD5KeyChainKeyStartGenerate_Object = MibTableColumn
rlMD5KeyChainKeyStartGenerate = _RlMD5KeyChainKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 5),
    _RlMD5KeyChainKeyStartGenerate_Type()
)
rlMD5KeyChainKeyStartGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStartGenerate.setStatus("current")
_RlMD5KeyChainKeyStopGenerate_Type = DateAndTime
_RlMD5KeyChainKeyStopGenerate_Object = MibTableColumn
rlMD5KeyChainKeyStopGenerate = _RlMD5KeyChainKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 6),
    _RlMD5KeyChainKeyStopGenerate_Type()
)
rlMD5KeyChainKeyStopGenerate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStopGenerate.setStatus("current")
_RlMD5KeyChainKeyStopAccept_Type = DateAndTime
_RlMD5KeyChainKeyStopAccept_Object = MibTableColumn
rlMD5KeyChainKeyStopAccept = _RlMD5KeyChainKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 7),
    _RlMD5KeyChainKeyStopAccept_Type()
)
rlMD5KeyChainKeyStopAccept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyStopAccept.setStatus("current")


class _RlMD5KeyChainKeyValidForAccept_Type(TruthValue):
    """Custom type rlMD5KeyChainKeyValidForAccept based on TruthValue"""
    defaultValue = 2


_RlMD5KeyChainKeyValidForAccept_Type.__name__ = "TruthValue"
_RlMD5KeyChainKeyValidForAccept_Object = MibTableColumn
rlMD5KeyChainKeyValidForAccept = _RlMD5KeyChainKeyValidForAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 8),
    _RlMD5KeyChainKeyValidForAccept_Type()
)
rlMD5KeyChainKeyValidForAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyValidForAccept.setStatus("current")


class _RlMD5KeyChainKeyValidForGenerate_Type(TruthValue):
    """Custom type rlMD5KeyChainKeyValidForGenerate based on TruthValue"""
    defaultValue = 2


_RlMD5KeyChainKeyValidForGenerate_Type.__name__ = "TruthValue"
_RlMD5KeyChainKeyValidForGenerate_Object = MibTableColumn
rlMD5KeyChainKeyValidForGenerate = _RlMD5KeyChainKeyValidForGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 9),
    _RlMD5KeyChainKeyValidForGenerate_Type()
)
rlMD5KeyChainKeyValidForGenerate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMD5KeyChainKeyValidForGenerate.setStatus("current")
_RlMD5KeyChainRowStatus_Type = RowStatus
_RlMD5KeyChainRowStatus_Object = MibTableColumn
rlMD5KeyChainRowStatus = _RlMD5KeyChainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 10),
    _RlMD5KeyChainRowStatus_Type()
)
rlMD5KeyChainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMD5KeyChainRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DIGITALKEYMANAGE-MIB",
    **{"rlDigitalKeyManage": rlDigitalKeyManage,
       "rlMD5KeyChainTable": rlMD5KeyChainTable,
       "rlMD5KeyChainEntry": rlMD5KeyChainEntry,
       "rlMD5KeyChainName": rlMD5KeyChainName,
       "rlMD5KeyChainKeyId": rlMD5KeyChainKeyId,
       "rlMD5KeyChainKey": rlMD5KeyChainKey,
       "rlMD5KeyChainKeyStartAccept": rlMD5KeyChainKeyStartAccept,
       "rlMD5KeyChainKeyStartGenerate": rlMD5KeyChainKeyStartGenerate,
       "rlMD5KeyChainKeyStopGenerate": rlMD5KeyChainKeyStopGenerate,
       "rlMD5KeyChainKeyStopAccept": rlMD5KeyChainKeyStopAccept,
       "rlMD5KeyChainKeyValidForAccept": rlMD5KeyChainKeyValidForAccept,
       "rlMD5KeyChainKeyValidForGenerate": rlMD5KeyChainKeyValidForGenerate,
       "rlMD5KeyChainRowStatus": rlMD5KeyChainRowStatus}
)
