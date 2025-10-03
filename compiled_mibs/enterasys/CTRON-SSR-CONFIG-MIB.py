# SNMP MIB module (CTRON-SSR-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SSR-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:46 2025
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ssrConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230)
)
if mibBuilder.loadTexts:
    ssrConfigMIB.setRevisions(
        ("2000-07-15 00:00",
         "2000-02-20 00:00",
         "1998-08-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SSRErrorCode(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 1),
          ("timeout", 2),
          ("networkError", 3),
          ("noSpace", 4),
          ("invalidConfig", 5),
          ("commandCompleted", 6),
          ("internalError", 7),
          ("tftpServerError", 8))
    )



# MIB Managed Objects in the order of their OIDs

_ConfigConformance_ObjectIdentity = ObjectIdentity
configConformance = _ConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3)
)
_ConfigCompliances_ObjectIdentity = ObjectIdentity
configCompliances = _ConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1)
)
_ConfigGroups_ObjectIdentity = ObjectIdentity
configGroups = _ConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2)
)
_CfgGroup_ObjectIdentity = ObjectIdentity
cfgGroup = _CfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231)
)


class _CfgTransferOp_Type(Integer32):
    """Custom type cfgTransferOp based on Integer32"""
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
        *(("noop", 1),
          ("sendConfigToAgent", 2),
          ("receiveConfigFromAgent", 3),
          ("receiveBootlogFromAgent", 4))
    )


_CfgTransferOp_Type.__name__ = "Integer32"
_CfgTransferOp_Object = MibScalar
cfgTransferOp = _CfgTransferOp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 1),
    _CfgTransferOp_Type()
)
cfgTransferOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgTransferOp.setStatus("current")
_CfgManagerAddress_Type = IpAddress
_CfgManagerAddress_Object = MibScalar
cfgManagerAddress = _CfgManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 2),
    _CfgManagerAddress_Type()
)
cfgManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgManagerAddress.setStatus("current")
_CfgFileName_Type = DisplayString
_CfgFileName_Object = MibScalar
cfgFileName = _CfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 3),
    _CfgFileName_Type()
)
cfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFileName.setStatus("current")
_CfgActivateTransfer_Type = TruthValue
_CfgActivateTransfer_Object = MibScalar
cfgActivateTransfer = _CfgActivateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 4),
    _CfgActivateTransfer_Type()
)
cfgActivateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgActivateTransfer.setStatus("current")


class _CfgTransferStatus_Type(Integer32):
    """Custom type cfgTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("sending", 2),
          ("receiving", 3),
          ("transferComplete", 4),
          ("error", 5))
    )


_CfgTransferStatus_Type.__name__ = "Integer32"
_CfgTransferStatus_Object = MibScalar
cfgTransferStatus = _CfgTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 5),
    _CfgTransferStatus_Type()
)
cfgTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgTransferStatus.setStatus("current")
_CfgActivateFile_Type = TruthValue
_CfgActivateFile_Object = MibScalar
cfgActivateFile = _CfgActivateFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 6),
    _CfgActivateFile_Type()
)
cfgActivateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgActivateFile.setStatus("current")
_CfgLastError_Type = SSRErrorCode
_CfgLastError_Object = MibScalar
cfgLastError = _CfgLastError_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 7),
    _CfgLastError_Type()
)
cfgLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgLastError.setStatus("current")
_CfgLastErrorReason_Type = DisplayString
_CfgLastErrorReason_Object = MibScalar
cfgLastErrorReason = _CfgLastErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 8),
    _CfgLastErrorReason_Type()
)
cfgLastErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgLastErrorReason.setStatus("current")
_CfgActiveImageVersion_Type = DisplayString
_CfgActiveImageVersion_Object = MibScalar
cfgActiveImageVersion = _CfgActiveImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 9),
    _CfgActiveImageVersion_Type()
)
cfgActiveImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgActiveImageVersion.setStatus("current")
_CfgActiveImageBootLocation_Type = DisplayString
_CfgActiveImageBootLocation_Object = MibScalar
cfgActiveImageBootLocation = _CfgActiveImageBootLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 10),
    _CfgActiveImageBootLocation_Type()
)
cfgActiveImageBootLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgActiveImageBootLocation.setStatus("current")

# Managed Objects groups

configGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 1)
)
configGroup10.setObjects(
      *(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"),
        ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"),
        ("CTRON-SSR-CONFIG-MIB", "cfgFileName"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"),
        ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"),
        ("CTRON-SSR-CONFIG-MIB", "cfgLastError"),
        ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"))
)
if mibBuilder.loadTexts:
    configGroup10.setStatus("deprecated")

configGroup20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 2)
)
configGroup20.setObjects(
      *(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"),
        ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"),
        ("CTRON-SSR-CONFIG-MIB", "cfgFileName"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"),
        ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"),
        ("CTRON-SSR-CONFIG-MIB", "cfgLastError"),
        ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageVersion"),
        ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageBootLocation"))
)
if mibBuilder.loadTexts:
    configGroup20.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

configCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 1)
)
configCompliance.setObjects(
    ("CTRON-SSR-CONFIG-MIB", "configGroup10")
)
if mibBuilder.loadTexts:
    configCompliance.setStatus(
        "obsolete"
    )

configCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 2)
)
configCompliance2.setObjects(
    ("CTRON-SSR-CONFIG-MIB", "configGroup20")
)
if mibBuilder.loadTexts:
    configCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-CONFIG-MIB",
    **{"SSRErrorCode": SSRErrorCode,
       "ssrConfigMIB": ssrConfigMIB,
       "configConformance": configConformance,
       "configCompliances": configCompliances,
       "configCompliance": configCompliance,
       "configCompliance2": configCompliance2,
       "configGroups": configGroups,
       "configGroup10": configGroup10,
       "configGroup20": configGroup20,
       "cfgGroup": cfgGroup,
       "cfgTransferOp": cfgTransferOp,
       "cfgManagerAddress": cfgManagerAddress,
       "cfgFileName": cfgFileName,
       "cfgActivateTransfer": cfgActivateTransfer,
       "cfgTransferStatus": cfgTransferStatus,
       "cfgActivateFile": cfgActivateFile,
       "cfgLastError": cfgLastError,
       "cfgLastErrorReason": cfgLastErrorReason,
       "cfgActiveImageVersion": cfgActiveImageVersion,
       "cfgActiveImageBootLocation": cfgActiveImageBootLocation}
)
