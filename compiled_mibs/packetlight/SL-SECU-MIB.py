# SNMP MIB module (SL-SECU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-SECU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:05 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

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

slSecuMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlSecuType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2),
          ("http", 3),
          ("https", 4),
          ("icmp", 5),
          ("snmp", 6),
          ("ftp", 7),
          ("tftp", 8),
          ("tl1", 9),
          ("tl1ssh", 10),
          ("wl", 11),
          ("snmpovertcp", 12),
          ("sftp", 13))
    )



# MIB Managed Objects in the order of their OIDs

_SlSecuGen_ObjectIdentity = ObjectIdentity
slSecuGen = _SlSecuGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1)
)
_SlSecuFirewallEnable_Type = TruthValue
_SlSecuFirewallEnable_Object = MibScalar
slSecuFirewallEnable = _SlSecuFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1, 1),
    _SlSecuFirewallEnable_Type()
)
slSecuFirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuFirewallEnable.setStatus("current")
_SlSecuSelect_ObjectIdentity = ObjectIdentity
slSecuSelect = _SlSecuSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2)
)
_SlSecuSelectTable_Object = MibTable
slSecuSelectTable = _SlSecuSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1)
)
if mibBuilder.loadTexts:
    slSecuSelectTable.setStatus("current")
_SlSecuSelectEntry_Object = MibTableRow
slSecuSelectEntry = _SlSecuSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1)
)
slSecuSelectEntry.setIndexNames(
    (0, "SL-SECU-MIB", "slSecuSelectType"),
)
if mibBuilder.loadTexts:
    slSecuSelectEntry.setStatus("current")
_SlSecuSelectType_Type = SlSecuType
_SlSecuSelectType_Object = MibTableColumn
slSecuSelectType = _SlSecuSelectType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 1),
    _SlSecuSelectType_Type()
)
slSecuSelectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slSecuSelectType.setStatus("current")
_SlSecuSelectPort_Type = Integer32
_SlSecuSelectPort_Object = MibTableColumn
slSecuSelectPort = _SlSecuSelectPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 2),
    _SlSecuSelectPort_Type()
)
slSecuSelectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuSelectPort.setStatus("current")
_SlSecuSelectEnable_Type = TruthValue
_SlSecuSelectEnable_Object = MibTableColumn
slSecuSelectEnable = _SlSecuSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 3),
    _SlSecuSelectEnable_Type()
)
slSecuSelectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuSelectEnable.setStatus("current")
_SlSecuWl_ObjectIdentity = ObjectIdentity
slSecuWl = _SlSecuWl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3)
)
_SlSecuWlTable_Object = MibTable
slSecuWlTable = _SlSecuWlTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1)
)
if mibBuilder.loadTexts:
    slSecuWlTable.setStatus("current")
_SlSecuWlEntry_Object = MibTableRow
slSecuWlEntry = _SlSecuWlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1)
)
slSecuWlEntry.setIndexNames(
    (0, "SL-SECU-MIB", "slSecuWlIp"),
)
if mibBuilder.loadTexts:
    slSecuWlEntry.setStatus("current")
_SlSecuWlIp_Type = IpAddress
_SlSecuWlIp_Object = MibTableColumn
slSecuWlIp = _SlSecuWlIp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 1),
    _SlSecuWlIp_Type()
)
slSecuWlIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuWlIp.setStatus("current")
_SlSecuWlMask_Type = IpAddress
_SlSecuWlMask_Object = MibTableColumn
slSecuWlMask = _SlSecuWlMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 2),
    _SlSecuWlMask_Type()
)
slSecuWlMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuWlMask.setStatus("current")
_SlSecuWlStatus_Type = RowStatus
_SlSecuWlStatus_Object = MibTableColumn
slSecuWlStatus = _SlSecuWlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 3),
    _SlSecuWlStatus_Type()
)
slSecuWlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSecuWlStatus.setStatus("current")
_SlSecuEncryption_ObjectIdentity = ObjectIdentity
slSecuEncryption = _SlSecuEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4)
)
_SlSecuEncryptionTable_Object = MibTable
slSecuEncryptionTable = _SlSecuEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1)
)
if mibBuilder.loadTexts:
    slSecuEncryptionTable.setStatus("current")
_SlSecuEncryptionEntry_Object = MibTableRow
slSecuEncryptionEntry = _SlSecuEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1)
)
slSecuEncryptionEntry.setIndexNames(
    (0, "SL-SECU-MIB", "slSecuEncryptionIfIndex"),
)
if mibBuilder.loadTexts:
    slSecuEncryptionEntry.setStatus("current")
_SlSecuEncryptionIfIndex_Type = InterfaceIndex
_SlSecuEncryptionIfIndex_Object = MibTableColumn
slSecuEncryptionIfIndex = _SlSecuEncryptionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 1),
    _SlSecuEncryptionIfIndex_Type()
)
slSecuEncryptionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuEncryptionIfIndex.setStatus("current")
_SlSecuEncryptionEnable_Type = TruthValue
_SlSecuEncryptionEnable_Object = MibTableColumn
slSecuEncryptionEnable = _SlSecuEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 2),
    _SlSecuEncryptionEnable_Type()
)
slSecuEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuEncryptionEnable.setStatus("current")


class _SlSecuEncryptionStatus_Type(Integer32):
    """Custom type slSecuEncryptionStatus based on Integer32"""
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
        *(("init", 1),
          ("exchange", 2),
          ("kdf", 3),
          ("active", 4))
    )


_SlSecuEncryptionStatus_Type.__name__ = "Integer32"
_SlSecuEncryptionStatus_Object = MibTableColumn
slSecuEncryptionStatus = _SlSecuEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 3),
    _SlSecuEncryptionStatus_Type()
)
slSecuEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuEncryptionStatus.setStatus("current")
_SlSecuEncryptionForceInit_Type = Integer32
_SlSecuEncryptionForceInit_Object = MibTableColumn
slSecuEncryptionForceInit = _SlSecuEncryptionForceInit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 4),
    _SlSecuEncryptionForceInit_Type()
)
slSecuEncryptionForceInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuEncryptionForceInit.setStatus("current")
_SlSecuEncryptionPreShared_Type = DisplayString
_SlSecuEncryptionPreShared_Object = MibTableColumn
slSecuEncryptionPreShared = _SlSecuEncryptionPreShared_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 5),
    _SlSecuEncryptionPreShared_Type()
)
slSecuEncryptionPreShared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuEncryptionPreShared.setStatus("current")
_SlSecuEncryptionKeyExchangePeriod_Type = Integer32
_SlSecuEncryptionKeyExchangePeriod_Object = MibTableColumn
slSecuEncryptionKeyExchangePeriod = _SlSecuEncryptionKeyExchangePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 6),
    _SlSecuEncryptionKeyExchangePeriod_Type()
)
slSecuEncryptionKeyExchangePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuEncryptionKeyExchangePeriod.setStatus("current")
_SlSecuEncryptionLock_Type = TruthValue
_SlSecuEncryptionLock_Object = MibTableColumn
slSecuEncryptionLock = _SlSecuEncryptionLock_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 7),
    _SlSecuEncryptionLock_Type()
)
slSecuEncryptionLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSecuEncryptionLock.setStatus("current")


class _SlSecuEncryptionProtectedStatus_Type(Integer32):
    """Custom type slSecuEncryptionProtectedStatus based on Integer32"""
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
        *(("init", 1),
          ("exchange", 2),
          ("kdf", 3),
          ("active", 4))
    )


_SlSecuEncryptionProtectedStatus_Type.__name__ = "Integer32"
_SlSecuEncryptionProtectedStatus_Object = MibTableColumn
slSecuEncryptionProtectedStatus = _SlSecuEncryptionProtectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 8),
    _SlSecuEncryptionProtectedStatus_Type()
)
slSecuEncryptionProtectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSecuEncryptionProtectedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SECU-MIB",
    **{"SlSecuType": SlSecuType,
       "slSecuMib": slSecuMib,
       "slSecuGen": slSecuGen,
       "slSecuFirewallEnable": slSecuFirewallEnable,
       "slSecuSelect": slSecuSelect,
       "slSecuSelectTable": slSecuSelectTable,
       "slSecuSelectEntry": slSecuSelectEntry,
       "slSecuSelectType": slSecuSelectType,
       "slSecuSelectPort": slSecuSelectPort,
       "slSecuSelectEnable": slSecuSelectEnable,
       "slSecuWl": slSecuWl,
       "slSecuWlTable": slSecuWlTable,
       "slSecuWlEntry": slSecuWlEntry,
       "slSecuWlIp": slSecuWlIp,
       "slSecuWlMask": slSecuWlMask,
       "slSecuWlStatus": slSecuWlStatus,
       "slSecuEncryption": slSecuEncryption,
       "slSecuEncryptionTable": slSecuEncryptionTable,
       "slSecuEncryptionEntry": slSecuEncryptionEntry,
       "slSecuEncryptionIfIndex": slSecuEncryptionIfIndex,
       "slSecuEncryptionEnable": slSecuEncryptionEnable,
       "slSecuEncryptionStatus": slSecuEncryptionStatus,
       "slSecuEncryptionForceInit": slSecuEncryptionForceInit,
       "slSecuEncryptionPreShared": slSecuEncryptionPreShared,
       "slSecuEncryptionKeyExchangePeriod": slSecuEncryptionKeyExchangePeriod,
       "slSecuEncryptionLock": slSecuEncryptionLock,
       "slSecuEncryptionProtectedStatus": slSecuEncryptionProtectedStatus}
)
