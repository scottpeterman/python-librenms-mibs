# SNMP MIB module (CISCOSB-BANNER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-BANNER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:14 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rlBanner = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133)
)
if mibBuilder.loadTexts:
    rlBanner.setRevisions(
        ("2007-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BannerMessageType(TextualConvention, Integer32):
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
        *(("rlBannerMOTD", 1),
          ("rlBannerLogin", 2),
          ("rlBannerExec", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlBannerMessageTable_Object = MibTable
rlBannerMessageTable = _RlBannerMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1)
)
if mibBuilder.loadTexts:
    rlBannerMessageTable.setStatus("current")
_RlBannerMessageEntry_Object = MibTableRow
rlBannerMessageEntry = _RlBannerMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1)
)
rlBannerMessageEntry.setIndexNames(
    (0, "CISCOSB-BANNER-MIB", "rlBannerMessageType"),
    (0, "CISCOSB-BANNER-MIB", "rlBannerMessageIndex"),
)
if mibBuilder.loadTexts:
    rlBannerMessageEntry.setStatus("current")
_RlBannerMessageType_Type = BannerMessageType
_RlBannerMessageType_Object = MibTableColumn
rlBannerMessageType = _RlBannerMessageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 1),
    _RlBannerMessageType_Type()
)
rlBannerMessageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBannerMessageType.setStatus("current")


class _RlBannerMessageIndex_Type(Integer32):
    """Custom type rlBannerMessageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_RlBannerMessageIndex_Type.__name__ = "Integer32"
_RlBannerMessageIndex_Object = MibTableColumn
rlBannerMessageIndex = _RlBannerMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 2),
    _RlBannerMessageIndex_Type()
)
rlBannerMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBannerMessageIndex.setStatus("current")
_RlBannerMessageText_Type = SnmpAdminString
_RlBannerMessageText_Object = MibTableColumn
rlBannerMessageText = _RlBannerMessageText_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 3),
    _RlBannerMessageText_Type()
)
rlBannerMessageText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerMessageText.setStatus("current")
_RlBannerManageTable_Object = MibTable
rlBannerManageTable = _RlBannerManageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2)
)
if mibBuilder.loadTexts:
    rlBannerManageTable.setStatus("current")
_RlBannerManageEntry_Object = MibTableRow
rlBannerManageEntry = _RlBannerManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1)
)
rlBannerManageEntry.setIndexNames(
    (0, "CISCOSB-BANNER-MIB", "rlBannerMessageType"),
)
if mibBuilder.loadTexts:
    rlBannerManageEntry.setStatus("current")
_RlBannerManageSSH_Type = EnabledStatus
_RlBannerManageSSH_Object = MibTableColumn
rlBannerManageSSH = _RlBannerManageSSH_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 1),
    _RlBannerManageSSH_Type()
)
rlBannerManageSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageSSH.setStatus("current")
_RlBannerManageTelnet_Type = EnabledStatus
_RlBannerManageTelnet_Object = MibTableColumn
rlBannerManageTelnet = _RlBannerManageTelnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 2),
    _RlBannerManageTelnet_Type()
)
rlBannerManageTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageTelnet.setStatus("current")
_RlBannerManageConsole_Type = EnabledStatus
_RlBannerManageConsole_Object = MibTableColumn
rlBannerManageConsole = _RlBannerManageConsole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 3),
    _RlBannerManageConsole_Type()
)
rlBannerManageConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerManageConsole.setStatus("current")
_RlBannerMessageClear_Type = BannerMessageType
_RlBannerMessageClear_Object = MibScalar
rlBannerMessageClear = _RlBannerMessageClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 3),
    _RlBannerMessageClear_Type()
)
rlBannerMessageClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBannerMessageClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-BANNER-MIB",
    **{"BannerMessageType": BannerMessageType,
       "rlBanner": rlBanner,
       "rlBannerMessageTable": rlBannerMessageTable,
       "rlBannerMessageEntry": rlBannerMessageEntry,
       "rlBannerMessageType": rlBannerMessageType,
       "rlBannerMessageIndex": rlBannerMessageIndex,
       "rlBannerMessageText": rlBannerMessageText,
       "rlBannerManageTable": rlBannerManageTable,
       "rlBannerManageEntry": rlBannerManageEntry,
       "rlBannerManageSSH": rlBannerManageSSH,
       "rlBannerManageTelnet": rlBannerManageTelnet,
       "rlBannerManageConsole": rlBannerManageConsole,
       "rlBannerMessageClear": rlBannerMessageClear}
)
