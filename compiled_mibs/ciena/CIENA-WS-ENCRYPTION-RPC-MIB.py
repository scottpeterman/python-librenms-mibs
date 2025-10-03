# SNMP MIB module (CIENA-WS-ENCRYPTION-RPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-ENCRYPTION-RPC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:05 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cienaWsEncryptionRPCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24)
)
if mibBuilder.loadTexts:
    cienaWsEncryptionRPCMIB.setRevisions(
        ("2017-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsEncryptionRPCObjects_ObjectIdentity = ObjectIdentity
cienaWsEncryptionRPCObjects = _CienaWsEncryptionRPCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 1)
)
_CienaWsEncryptionRPCConformance_ObjectIdentity = ObjectIdentity
cienaWsEncryptionRPCConformance = _CienaWsEncryptionRPCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 2)
)
_CienaWsEncryptionRPCGroups_ObjectIdentity = ObjectIdentity
cienaWsEncryptionRPCGroups = _CienaWsEncryptionRPCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 2, 1)
)
_CienaWsEncryptionRPCCompliances_ObjectIdentity = ObjectIdentity
cienaWsEncryptionRPCCompliances = _CienaWsEncryptionRPCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 2, 2)
)
_CwsEncryptionRPCClearCSPTable_Object = MibTable
cwsEncryptionRPCClearCSPTable = _CwsEncryptionRPCClearCSPTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3)
)
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPTable.setStatus("current")
_CwsEncryptionRPCClearCSPEntry_Object = MibTableRow
cwsEncryptionRPCClearCSPEntry = _CwsEncryptionRPCClearCSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1)
)
cwsEncryptionRPCClearCSPEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCClearCSPSnmpIndex"),
)
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPEntry.setStatus("current")


class _CwsEncryptionRPCClearCSPSnmpIndex_Type(Integer32):
    """Custom type cwsEncryptionRPCClearCSPSnmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionRPCClearCSPSnmpIndex_Type.__name__ = "Integer32"
_CwsEncryptionRPCClearCSPSnmpIndex_Object = MibTableColumn
cwsEncryptionRPCClearCSPSnmpIndex = _CwsEncryptionRPCClearCSPSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1, 1),
    _CwsEncryptionRPCClearCSPSnmpIndex_Type()
)
cwsEncryptionRPCClearCSPSnmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPSnmpIndex.setStatus("current")


class _CwsEncryptionRPCClearCSPActivate_Type(Integer32):
    """Custom type cwsEncryptionRPCClearCSPActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("activate", 1))
    )


_CwsEncryptionRPCClearCSPActivate_Type.__name__ = "Integer32"
_CwsEncryptionRPCClearCSPActivate_Object = MibTableColumn
cwsEncryptionRPCClearCSPActivate = _CwsEncryptionRPCClearCSPActivate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1, 2),
    _CwsEncryptionRPCClearCSPActivate_Type()
)
cwsEncryptionRPCClearCSPActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPActivate.setStatus("current")
_CwsEncryptionRPCClearCSPLastActivation_Type = TimeStamp
_CwsEncryptionRPCClearCSPLastActivation_Object = MibTableColumn
cwsEncryptionRPCClearCSPLastActivation = _CwsEncryptionRPCClearCSPLastActivation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1, 3),
    _CwsEncryptionRPCClearCSPLastActivation_Type()
)
cwsEncryptionRPCClearCSPLastActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPLastActivation.setStatus("current")


class _CwsEncryptionRPCClearCSPLastReturnCode_Type(Integer32):
    """Custom type cwsEncryptionRPCClearCSPLastReturnCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("pass", 1))
    )


_CwsEncryptionRPCClearCSPLastReturnCode_Type.__name__ = "Integer32"
_CwsEncryptionRPCClearCSPLastReturnCode_Object = MibTableColumn
cwsEncryptionRPCClearCSPLastReturnCode = _CwsEncryptionRPCClearCSPLastReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1, 4),
    _CwsEncryptionRPCClearCSPLastReturnCode_Type()
)
cwsEncryptionRPCClearCSPLastReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPLastReturnCode.setStatus("current")
_CwsEncryptionRPCClearCSPLastFailureReason_Type = DisplayString
_CwsEncryptionRPCClearCSPLastFailureReason_Object = MibTableColumn
cwsEncryptionRPCClearCSPLastFailureReason = _CwsEncryptionRPCClearCSPLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 3, 1, 5),
    _CwsEncryptionRPCClearCSPLastFailureReason_Type()
)
cwsEncryptionRPCClearCSPLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCClearCSPLastFailureReason.setStatus("current")
_CwsEncryptionRPCEnableEncryptionTable_Object = MibTable
cwsEncryptionRPCEnableEncryptionTable = _CwsEncryptionRPCEnableEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4)
)
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionTable.setStatus("current")
_CwsEncryptionRPCEnableEncryptionEntry_Object = MibTableRow
cwsEncryptionRPCEnableEncryptionEntry = _CwsEncryptionRPCEnableEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1)
)
cwsEncryptionRPCEnableEncryptionEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCEnableEncryptionSnmpIndex"),
)
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionEntry.setStatus("current")


class _CwsEncryptionRPCEnableEncryptionSnmpIndex_Type(Integer32):
    """Custom type cwsEncryptionRPCEnableEncryptionSnmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionRPCEnableEncryptionSnmpIndex_Type.__name__ = "Integer32"
_CwsEncryptionRPCEnableEncryptionSnmpIndex_Object = MibTableColumn
cwsEncryptionRPCEnableEncryptionSnmpIndex = _CwsEncryptionRPCEnableEncryptionSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1, 1),
    _CwsEncryptionRPCEnableEncryptionSnmpIndex_Type()
)
cwsEncryptionRPCEnableEncryptionSnmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionSnmpIndex.setStatus("current")


class _CwsEncryptionRPCEnableEncryptionActivate_Type(Integer32):
    """Custom type cwsEncryptionRPCEnableEncryptionActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("activate", 1))
    )


_CwsEncryptionRPCEnableEncryptionActivate_Type.__name__ = "Integer32"
_CwsEncryptionRPCEnableEncryptionActivate_Object = MibTableColumn
cwsEncryptionRPCEnableEncryptionActivate = _CwsEncryptionRPCEnableEncryptionActivate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1, 2),
    _CwsEncryptionRPCEnableEncryptionActivate_Type()
)
cwsEncryptionRPCEnableEncryptionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionActivate.setStatus("current")
_CwsEncryptionRPCEnableEncryptionLastActivation_Type = TimeStamp
_CwsEncryptionRPCEnableEncryptionLastActivation_Object = MibTableColumn
cwsEncryptionRPCEnableEncryptionLastActivation = _CwsEncryptionRPCEnableEncryptionLastActivation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1, 3),
    _CwsEncryptionRPCEnableEncryptionLastActivation_Type()
)
cwsEncryptionRPCEnableEncryptionLastActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionLastActivation.setStatus("current")


class _CwsEncryptionRPCEnableEncryptionLastReturnCode_Type(Integer32):
    """Custom type cwsEncryptionRPCEnableEncryptionLastReturnCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("pass", 1))
    )


_CwsEncryptionRPCEnableEncryptionLastReturnCode_Type.__name__ = "Integer32"
_CwsEncryptionRPCEnableEncryptionLastReturnCode_Object = MibTableColumn
cwsEncryptionRPCEnableEncryptionLastReturnCode = _CwsEncryptionRPCEnableEncryptionLastReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1, 4),
    _CwsEncryptionRPCEnableEncryptionLastReturnCode_Type()
)
cwsEncryptionRPCEnableEncryptionLastReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionLastReturnCode.setStatus("current")
_CwsEncryptionRPCEnableEncryptionLastFailureReason_Type = DisplayString
_CwsEncryptionRPCEnableEncryptionLastFailureReason_Object = MibTableColumn
cwsEncryptionRPCEnableEncryptionLastFailureReason = _CwsEncryptionRPCEnableEncryptionLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 4, 1, 5),
    _CwsEncryptionRPCEnableEncryptionLastFailureReason_Type()
)
cwsEncryptionRPCEnableEncryptionLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionRPCEnableEncryptionLastFailureReason.setStatus("current")

# Managed Objects groups

cienaWsEncryptionRPCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 2, 1, 1)
)
cienaWsEncryptionRPCGroup.setObjects(
      *(("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCClearCSPActivate"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCClearCSPLastActivation"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCClearCSPLastReturnCode"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCClearCSPLastFailureReason"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCEnableEncryptionActivate"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCEnableEncryptionLastActivation"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCEnableEncryptionLastReturnCode"),
        ("CIENA-WS-ENCRYPTION-RPC-MIB", "cwsEncryptionRPCEnableEncryptionLastFailureReason"))
)
if mibBuilder.loadTexts:
    cienaWsEncryptionRPCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsEncryptionRPCCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 24, 2, 2, 1)
)
cienaWsEncryptionRPCCompliance.setObjects(
    ("CIENA-WS-ENCRYPTION-RPC-MIB", "cienaWsEncryptionRPCGroup")
)
if mibBuilder.loadTexts:
    cienaWsEncryptionRPCCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-ENCRYPTION-RPC-MIB",
    **{"cienaWsEncryptionRPCMIB": cienaWsEncryptionRPCMIB,
       "cienaWsEncryptionRPCObjects": cienaWsEncryptionRPCObjects,
       "cienaWsEncryptionRPCConformance": cienaWsEncryptionRPCConformance,
       "cienaWsEncryptionRPCGroups": cienaWsEncryptionRPCGroups,
       "cienaWsEncryptionRPCGroup": cienaWsEncryptionRPCGroup,
       "cienaWsEncryptionRPCCompliances": cienaWsEncryptionRPCCompliances,
       "cienaWsEncryptionRPCCompliance": cienaWsEncryptionRPCCompliance,
       "cwsEncryptionRPCClearCSPTable": cwsEncryptionRPCClearCSPTable,
       "cwsEncryptionRPCClearCSPEntry": cwsEncryptionRPCClearCSPEntry,
       "cwsEncryptionRPCClearCSPSnmpIndex": cwsEncryptionRPCClearCSPSnmpIndex,
       "cwsEncryptionRPCClearCSPActivate": cwsEncryptionRPCClearCSPActivate,
       "cwsEncryptionRPCClearCSPLastActivation": cwsEncryptionRPCClearCSPLastActivation,
       "cwsEncryptionRPCClearCSPLastReturnCode": cwsEncryptionRPCClearCSPLastReturnCode,
       "cwsEncryptionRPCClearCSPLastFailureReason": cwsEncryptionRPCClearCSPLastFailureReason,
       "cwsEncryptionRPCEnableEncryptionTable": cwsEncryptionRPCEnableEncryptionTable,
       "cwsEncryptionRPCEnableEncryptionEntry": cwsEncryptionRPCEnableEncryptionEntry,
       "cwsEncryptionRPCEnableEncryptionSnmpIndex": cwsEncryptionRPCEnableEncryptionSnmpIndex,
       "cwsEncryptionRPCEnableEncryptionActivate": cwsEncryptionRPCEnableEncryptionActivate,
       "cwsEncryptionRPCEnableEncryptionLastActivation": cwsEncryptionRPCEnableEncryptionLastActivation,
       "cwsEncryptionRPCEnableEncryptionLastReturnCode": cwsEncryptionRPCEnableEncryptionLastReturnCode,
       "cwsEncryptionRPCEnableEncryptionLastFailureReason": cwsEncryptionRPCEnableEncryptionLastFailureReason}
)
